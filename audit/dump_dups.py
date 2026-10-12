import sys, os, csv, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_engine as E, audit_full as F
subj = sys.argv[1]; d = os.path.join(F.HERE, F.SLUG[subj])
bank = {x['id']: x for x in E.load() if x['_subj'] == subj}
def line(x):
    a = x['answer']; o = x['options']
    if x['question_type'] in ('multiple_choice', 'multiple_choice_visual', 'contextual'): a = o['ABCD'.index(a)]
    elif isinstance(a, (dict, list)): a = json.dumps(a, ensure_ascii=False)[:100]
    return f"{x['question_type'][:4]}|{x['question']}|=> {a}"
for r in csv.DictReader(open(os.path.join(d, 'DUPLICATION_REPORT.csv'), encoding='utf-8')):
    a, b = bank[r['id_1']], bank[r['id_2']]
    print(f"{r['id_1']} ~ {r['id_2']} ({r['kemiripan']})\n   A {line(a)}\n   B {line(b)}")
