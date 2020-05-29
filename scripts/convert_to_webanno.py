import json

BARCODE_A = 'Z257381902'
BARCODE_B = 'Z159574205'

"""
Each pair looks like this:

"a": {
  "start": 6120,
  "end": 6189,
  "text": "er chtzenbeylangem Lebenbetndiger Geundheit vnd allem HochFrtlihe "
},
"b": {
  "start": 6734,
  "end": 6804,
  "text": " Familie bey angem Leben bendjger Gefundheit und allem hohen Wo ere"
}
"""
def to_annotation(id, passage):
  return {
    "@context": "http://www.w3.org/ns/anno.jsonld",
    "id": id,
    "type": "Annotation",
    "body": [{
      "type": "TextualBody",
      "value": passage['text']
    }],
    "target": {
      "selector": {
        "type": "TextPositionSelector",
        "start": passage['start'],
        "end": passage['end']
      }
    }
  }

annotations_a = []
annotations_b = []

with open(f'../sample-data/alignment_{BARCODE_A}_{BARCODE_B}.json', 'r') as infile:
  alignments = json.load(infile)

  for idx, pair in enumerate(alignments):
    annotations_a.append(to_annotation(f'left_{idx}', pair['a']))
    annotations_b.append(to_annotation(f'right_{idx}', pair['b']))

with open(f'../sample-data/annotations.{BARCODE_A}.json', 'w') as out_a:
  json.dump(annotations_a, out_a, indent=2)

with open(f'../sample-data/annotations.{BARCODE_B}.json', 'w') as out_b:
  json.dump(annotations_b, out_b, indent=2)
