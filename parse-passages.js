/**
 * Converts a data file with aligned passages to two sets of 
 * W3C Web Annotations.
 */
function parseAlignedPassages(passage_data) {

  // Helper to convert a passage data record to WebAnno
  function toAnnotation(id, passage) {
    return {
      "@context": "http://www.w3.org/ns/anno.jsonld",
      "id": id,
      "type": "Annotation",
      "body": [{
        "type": "TextualBody",
        "value": passage.text
      }],
      "target": {
        "selector": [{
          "type": "TextQuoteSelector",
          "exact": passage.text
        },{
          "type": "TextPositionSelector",
          "start": passage.start,
          "end": passage.end
        }]
      }
    }
  }

  // Maps the left passage side to WebAnno
  var left = passage_data.map(function(pair, idx) { 
    var id = 'left_' + idx;
    return toAnnotation(id, pair.a) 
  });
  
  // Maps the right passage side to WebAnno
  var right = passage_data.map(function(pair, idx) { 
    var id = 'right_' + idx;
    return toAnnotation(id, pair.b);
  });

  return { left, right };
}