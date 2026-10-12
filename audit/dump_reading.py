import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_engine as E
subj, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
items = [x for x in E.load() if x['_subj'] == subj][a:b]
for x in items:
    t = x['question_type']; o = x['options']; ans = x['answer']
    if t in ('multiple_choice', 'multiple_choice_visual', 'contextual'):
        opt = ' / '.join(('*' if s[0] == ans else '') + s for s in o); k = ''
    elif t == 'true_false': opt = ''; k = ans
    elif t in ('matching',): opt = ''; k = '; '.join(f'{p}->{q}' for p, q in ans.items())
    elif t == 'grouping': opt = ''; k = '; '.join(f"{g}:{','.join(v)}" for g, v in ans.items())
    elif t == 'ordering': opt = ''; k = ' > '.join(ans)
    elif t == 'performance_task': opt = ''; k = 'rubrik'
    else: opt = ''; k = ans
    tp = x['tp_id'].split('-', 2)[2]
    vis = f" [GAMBAR: {x['visual_prompt']}]" if x['visual_required'] else ''
    print(f"{x['id'][4:]}|{tp}|{t[:4]}|{x['difficulty'][0]}|{x['question']}{vis}|{opt}{k}")
