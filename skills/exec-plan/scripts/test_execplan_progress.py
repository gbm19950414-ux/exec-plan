import copy
import hashlib
from pathlib import Path
import tempfile
import unittest
from execplan_progress import block, inspect, parse, publication, publish, ProgressError

def record(pid='plan-one', gid='goal-one'):
    return {'schema': 'execplan-progress/v1', 'plan_id': pid, 'goal_id': gid, 'project_id': 'project',
            'title': 'A plan', 'objective': 'Observable result', 'execution_status': 'active',
            'assessment': {'outcome': 'insufficient_evidence', 'summary': 'User trial pending', 'evidence': []},
            'milestones': [{'id': 'm1', 'title': 'Implementation', 'state': 'done', 'depends_on': [], 'evidence': ['tests passed']}],
            'next_action': 'User trial', 'updated_at': '2026-09-28T00:00:00Z', 'published_sha256': ''}


def document(value=None):
    return publication('# Plan\n\n## Progress\n\n' + block(value or record()) + '\n\n## Outcomes & Retrospective\n\nPending user feedback.\n')


class ProgressTests(unittest.TestCase):
    def test_publication_covers_prose_summary_and_json_and_is_idempotent(self):
        text = document()
        self.assertEqual(inspect(text)['status'], 'synced')
        self.assertEqual(publication(text), text)
        for before, after in [('Pending user feedback.', 'Changed scope.'), ('[完成]', '[未知]'), ('User trial', 'New trial')]:
            self.assertEqual(inspect(text.replace(before, after))['status'], 'pending')
        self.assertEqual(parse(text)['assessment']['outcome'], 'insufficient_evidence')
        self.assertEqual(inspect('## Progress\n- [x] old plan')['status'], 'legacy')

    def test_invalid_identity_dependencies_evidence_and_version(self):
        for mutate in [lambda r: r.update(schema='future'),
                       lambda r: r['milestones'].append(copy.deepcopy(r['milestones'][0])),
                       lambda r: r['milestones'][0].update(depends_on=['missing']),
                       lambda r: r['milestones'][0].update(depends_on=['m1']),
                       lambda r: r['assessment'].update(outcome='met')]:
            r = record(); mutate(r)
            with self.assertRaises(ProgressError): document(r)
        r = record(); r['milestones'].append(dict(r['milestones'][0], id='m2', depends_on=['m1'])); r['milestones'][0]['depends_on'] = ['m2']
        with self.assertRaises(ProgressError): document(r)

    def test_readonly_check_and_optimistic_atomic_publish(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'plan.md'; p.write_text(document())
            before = p.read_bytes(); inspect(before.decode()); self.assertEqual(before, p.read_bytes())
            p.write_text(p.read_text() + '\nnew discovery\n')
            with self.assertRaises(ProgressError): publish(p, hashlib.sha256(before).hexdigest())
            self.assertIn('new discovery', p.read_text())
            self.assertEqual(publish(p)['status'], 'synced')
            r = parse(p.read_text()); r['execution_status'] = 'closed'
            self.assertEqual(parse(document(r))['assessment']['outcome'], 'insufficient_evidence')



if __name__ == "__main__": unittest.main()
