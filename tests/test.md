```shell
curl http://127.0.0.1:8000/available_models
curl http://127.0.0.1:8000/loaded_models

---

curl http://127.0.0.1:8000/model/add_info \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-anything" \
  -d '{
  "model_name": "llama3",
  "model_type": "LlamacppLLM",
  "model_path": "/Users/wumengsong/Resource/gguf/Meta-Llama-3.1-8B-Instruct-Q8_0.gguf"
}'

curl http://127.0.0.1:8000/model/load/llama3 -H "Authorization: Bearer sk-anything"

curl http://127.0.0.1:8000/model/call/llama3 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-anything" \
  -d '{
  "input_text": "Do you know something about Dota2?",
  "max_new_tokens": 10
}'

curl http://127.0.0.1:8000/model/generate/llama3 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-anything" \
  -d '{
  "input_text": "Do you know something about Dota2?",
  "max_new_tokens": 5,
  "return_logits": true,
  "stop_strings": ["\n"]
}'

---

curl http://127.0.0.1:8000/model/add_info \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-anything" \
  -d '{
  "model_name": "gemma2",
  "model_type": "TransformersCausalLM",
  "model_path": "/Users/wumengsong/Resource/gemma-2-2b"
}'

curl http://127.0.0.1:8000/model/load/gemma2 -H "Authorization: Bearer sk-anything"

curl http://127.0.0.1:8000/model/call/gemma2 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-anything" \
  -d '{
  "input_text": "Do you know something about Dota2?",
  "max_new_tokens": 2
}'

curl http://127.0.0.1:8000/model/generate/gemma2 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-anything" \
  -d '{
  "input_text": "Do you know something about Dota2?",
  "max_new_tokens": 5,
  "return_logits": true,
  "stop_strings": ["\n"]
}'

curl http://127.0.0.1:8000/openai/chat/completions -H "Content-Type: application/json"   -H "Authorization: Bearer sk-anything" -d '{
  "model": "gemma2",
  "messages": [
    {
      "role": "system",
      "content": "You are a test assistant."
    },
    {
      "role": "user",
      "content": "Do you know something about Dota2?"
    }
  ],
  "max_completion_tokens": 2
}'
```

```shell
curl http://10.140.24.104:10001/available_models
curl http://10.140.24.104:10001/loaded_models
curl http://10.140.24.104:10001/model/add_info \
  -H "Content-Type: application/json" \
  -d '{
  "model_name": "gemma2",
  "model_type": "TransformersCausalLM",
  "model_path": "/Users/wumengsong/Resource/gemma-2-2b"
}'

curl http://10.140.24.104:10001/model/load/ChemLLM

```

```json
# llama.cpp
{
  "output_text":" That's a great game",
  "input_id_list":[128000,5519,499,1440,2555,922,86227,17,30],
  "input_token_list":["<|begin_of_text|>","Do"," you"," know"," something"," about"," Dota","2","?"],
  "input_text":"Do you know something about Dota2?",
  "full_id_list":[128000,5519,499,1440,2555,922,86227,17,30,3011,596,264,2294,1847],
  "full_token_list":["<|begin_of_text|>","Do"," you"," know"," something"," about"," Dota","2","?"," That","'s"," a"," great"," game"],
  "full_text":"Do you know something about Dota2? That's a great game",
  "logits":[
    {"id":128000,"token":"<|begin_of_text|>"},
    {"id":5519,"token":"Do"},
    {"id":499,"token":" you","pred_id":[499,510,1472,6978,279,539,6372,41529,358,4442],"pred_token":[" you"," ["," You"," patients"," the"," not"," effects"," serum"," I"," changes"],"logits":[],"probs":[0.1061,0.0168,0.0112,0.0109,0.0076,0.0075,0.0066,0.0057,0.0056,0.005],"logprobs":[-2.243,-4.0886,-4.4879,-4.5226,-4.8823,-4.8883,-5.014,-5.1651,-5.1867,-5.2909]},
    {"id":1440,"token":" know","pred_id":[617,1390,1440,1205,3596,3021,6227,2733,1781,1093],"pred_token":[" have"," want"," know"," need"," ever"," love"," remember"," feel"," think"," like"],"logits":[],"probs":[0.3157,0.1503,0.1271,0.0692,0.0508,0.0255,0.0195,0.0191,0.0189,0.0184],"logprobs":[-1.1531,-1.8951,-2.0629,-2.6711,-2.9797,-3.6709,-3.9358,-3.958,-3.969,-3.9938]},
    {"id":2555,"token":" something","pred_id":[1148,279,1268,430,4423,264,701,889,1405,922,2555],"pred_token":[" what"," the"," how"," that"," someone"," a"," your"," who"," where"," about"," something"],"logits":[],"probs":[0.2552,0.1598,0.1272,0.0869,0.0592,0.0302,0.0266,0.0265,0.025,0.0233,0.0025],"logprobs":[-1.3656,-1.8341,-2.0622,-2.4435,-2.8265,-3.5003,-3.6276,-3.6291,-3.6887,-3.7607,-6.0085]},
    {"id":922,"token":" about","pred_id":[922,430,358,584,374,499,30,701,279,5380],"pred_token":[" about"," that"," I"," we"," is"," you","?"," your"," the","?\n"],"logits":[],"probs":[0.3876,0.2977,0.0651,0.0599,0.0208,0.0193,0.0117,0.0081,0.0081,0.0065],"logprobs":[-0.9479,-1.2117,-2.7316,-2.8151,-3.8735,-3.9481,-4.445,-4.8141,-4.8218,-5.0403]},
    {"id":86227,"token":" Dota","pred_id":[279,420,264,701,1521,1057,459,330,6261,1268,86227],"pred_token":[" the"," this"," a"," your"," these"," our"," an"," \""," yourself"," how"," Dota"],"logits":[],"probs":[0.1099,0.0872,0.0281,0.01,0.0074,0.0047,0.004,0.0034,0.0031,0.0024,0.0],"logprobs":[-2.2085,-2.4401,-3.5727,-4.6009,-4.9001,-5.3572,-5.5253,-5.6984,-5.7854,-6.0182,-13.1288]},
    {"id":17,"token":"2","pred_id":[220,17,5380,9156,30,1322,9636,11,596,25],"pred_token":[" ","2","?\n"," Auto","?"," Pro"," Under",",","'s",":"],"logits":[],"probs":[0.8083,0.0272,0.0168,0.0115,0.0114,0.011,0.0077,0.0067,0.0041,0.0027],"logprobs":[-0.2128,-3.6045,-4.0879,-4.4666,-4.4777,-4.5143,-4.8664,-5.0039,-5.5071,-5.9287]},
    {"id":30,"token":"?","pred_id":[5380,30,323,11,477,430,596,949,1847,18072],"pred_token":["?\n","?"," and",","," or"," that","'s"," ?"," game"," ?\n"],"logits":[],"probs":[0.2447,0.1971,0.0479,0.0441,0.0426,0.0278,0.0239,0.0146,0.0145,0.0125],"logprobs":[-1.4078,-1.6238,-3.0381,-3.1204,-3.1565,-3.5822,-3.7328,-4.2284,-4.232,-4.3857]},
    {"id":3011,"token":" That","pred_id":[86227,1442,358,3234,1102,8489,1115,2582,1472,578,3011],"pred_token":[" Dota"," If"," I"," Do"," It"," Well"," This"," Or"," You"," The"," That"],"logits":[],"probs":[0.0995,0.0728,0.0633,0.0582,0.0322,0.0264,0.0233,0.0192,0.019,0.0172,0.0073],"logprobs":[-2.3079,-2.6194,-2.7599,-2.8447,-3.4353,-3.6338,-3.7609,-3.9519,-3.9631,-4.0606,-4.9263]},
    {"id":596,"token":"'s","pred_id":[596,1847,753,374,279,433,420,499,832,11672],"pred_token":["'s"," game","’s"," is"," the"," it"," this"," you"," one"," MO"],"logits":[],"probs":[0.3328,0.118,0.1093,0.1058,0.0169,0.0149,0.0098,0.0097,0.0092,0.0084],"logprobs":[-1.1001,-2.1368,-2.2138,-2.2459,-4.083,-4.204,-4.6209,-4.6383,-4.6916,-4.7839]},
    {"id":264,"token":" a","pred_id":[264,279,1314,459,1148,2294,3249,832,856,539],"pred_token":[" a"," the"," right"," an"," what"," great"," why"," one"," my"," not"],"logits":[],"probs":[0.3106,0.1275,0.0939,0.0448,0.0417,0.0335,0.0308,0.0245,0.0244,0.0239],"logprobs":[-1.1691,-2.0595,-2.3658,-3.1057,-3.1784,-3.3977,-3.4793,-3.7096,-3.7147,-3.7336]},
    {"id":2294,"token":" great","pred_id":[1847,5526,2294,39828,11672,1633,2216,5128,2466,6908],"pred_token":[" game"," popular"," great"," multiplayer"," MO"," very"," really"," pretty"," big"," huge"],"logits":[],"probs":[0.1496,0.1179,0.0874,0.0855,0.058,0.0531,0.0291,0.029,0.0172,0.0157],"logprobs":[-1.8996,-2.1376,-2.4369,-2.4596,-2.8467,-2.9365,-3.5383,-3.5388,-4.0605,-4.1558]},
    {"id":1847,"token":" game","pred_id":[1847,11672,3488,39828,8712,3245,1212,1648,8446,5873],"pred_token":[" game"," MO"," question"," multiplayer"," topic"," thing"," start"," way"," strategy"," choice"],"logits":[],"probs":[0.682,0.0363,0.0305,0.0162,0.0132,0.011,0.0084,0.0068,0.0068,0.0067],"logprobs":[-0.3828,-3.3147,-3.4899,-4.125,-4.3293,-4.5074,-4.7777,-4.9904,-4.9976,-5.0058]}]}
```


---


```json
# transformers
{
  "output_text":"\n\n",
  "input_id_list":[2,2795,692,1230,2775,1105,156348,235284,235336],
  "input_token_list":["<bos>","Do"," you"," know"," something"," about"," Dota","2","?"],"input_text":"Do you know something about Dota2?",
  "full_id_list":[2,2795,692,1230,2775,1105,156348,235284,235336,109],
  "full_token_list":["<bos>","Do"," you"," know"," something"," about"," Dota","2","?","\n\n"],
  "full_text":"Do you know something about Dota2?\n\n",
  "logits":[
    {"id":2,"token":"<bos>"},
    {"id":2795,"token":"Do","pred_id":[185,199,651,186,235322,2094,809,187,235280,201],"pred_token":["<h1>","<strong>","The","<h2>","<","package","import","<h3>","A","<b>"],"logits":[2.9247,2.3852,2.268,2.127,2.0123,1.8803,1.7142,1.382,1.3202,1.2289],"probs":[0.1356,0.079,0.0703,0.0611,0.0544,0.0477,0.0404,0.029,0.0272,0.0249],"logprobs":[]},
    {"id":692,"token":" you","pred_id":[692,9035,780,502,590,573,783,1646,861,46674],"pred_token":[" you","zens"," not","is"," I"," the"," we"," You"," your","lores"],"logits":[28.001,25.3857,24.8831,24.3304,24.1106,23.8864,23.8829,23.8625,23.7162,23.0279],"probs":[0.7325,0.0536,0.0324,0.0187,0.015,0.012,0.0119,0.0117,0.0101,0.0051],"logprobs":[]},
    {"id":1230,"token":" know","pred_id":[791,1938,1230,3364,1476,5434,1154,2182,1742,2375],"pred_token":[" have"," want"," know"," ever"," need"," remember"," like"," love"," think"," feel"],"logits":[28.4567,28.3359,28.0499,27.2119,27.1227,27.1215,26.9961,26.96,26.8413,26.4892],"probs":[0.1862,0.1651,0.124,0.0536,0.0491,0.049,0.0432,0.0417,0.037,0.026],"logprobs":[]},
    {"id":2775,"token":" something","pred_id":[1212,573,674,1368,3165,1105,4630,1064,476,861],"pred_token":[" what"," the"," that"," how"," why"," about"," someone"," who"," a"," your"],"logits":[28.7546,28.1733,28.1673,28.1651,26.8442,26.8069,26.7523,26.6916,26.6767,26.6281],"probs":[0.2218,0.124,0.1233,0.123,0.0328,0.0316,0.03,0.0282,0.0278,0.0265],"logprobs":[]},
    {"id":1105,"token":" about","pred_id":[1105,674,603,235336,692,590,3186,783,7103,235269],"pred_token":[" about"," that"," is","?"," you"," I"," special"," we"," interesting",","],"logits":[29.2221,27.8494,27.1968,27.1393,26.4338,25.9685,25.8194,25.7746,25.5683,25.5507],"probs":[0.4762,0.1207,0.0628,0.0593,0.0293,0.0184,0.0158,0.0152,0.0123,0.0121],"logprobs":[]},
    {"id":156348,"token":" Dota","pred_id":[573,861,736,235248,476,1167,1368,665,682,1212],"pred_token":[" the"," your"," this"," "," a"," our"," how"," it"," me"," what"],"logits":[29.2473,27.7965,27.4384,27.2761,27.0552,26.4016,26.3534,26.3077,26.1903,26.1073],"probs":[0.4298,0.1007,0.0704,0.0599,0.048,0.025,0.0238,0.0227,0.0202,0.0186],"logprobs":[]},
    {"id":235284,"token":"2","pred_id":[235248,235336,235284,235269,578,7457,674,689,235349,1362],"pred_token":[" ","?","2",","," and"," Under"," that"," or","’"," under"],"logits":[27.1342,25.263,24.6433,23.4623,23.2405,23.0928,22.7618,22.6227,22.2998,22.2694],"probs":[0.6913,0.1064,0.0573,0.0176,0.0141,0.0121,0.0087,0.0076,0.0055,0.0053],"logprobs":[]},
    {"id":235336,"token":"?","pred_id":[235336,235269,578,674,901,45366,689,1654,2398,235349],"pred_token":["?",","," and"," that"," but"," betting"," or"," ?"," game","’"],"logits":[28.3273,26.2681,26.1182,25.799,25.4272,25.4022,25.2717,25.0221,24.2714,24.1961],"probs":[0.5128,0.0654,0.0563,0.0409,0.0282,0.0275,0.0241,0.0188,0.0089,0.0082],"logprobs":[]},
    {"id":109,"token":"\n\n","pred_id":[109,1927,2390,108,590,156348,1646,5881,1417,1165],"pred_token":["\n\n"," If"," Do","\n"," I"," Dota"," You"," Are"," This"," It"],"logits":[28.757,28.2411,28.0566,27.6529,27.0933,26.9901,26.9742,26.9576,26.7798,26.7398],"probs":[0.1734,0.1035,0.0861,0.0575,0.0329,0.0296,0.0292,0.0287,0.024,0.0231],"logprobs":[]}]}
```