from jsonpath_ng import parse
import collections.abc

v2TraitPaths = [
  '$.channels.*.[publish,subscribe]',
  '$.components.channels.*.[publish,subscribe]',
  '$.channels.*.[publish,subscribe].message',
  '$.channels.*.[publish,subscribe].message.oneOf[*]',
  '$.components.channels.*.[publish,subscribe].message',
  '$.components.channels.*.[publish,subscribe].message.oneOf[*]',
  '$.components.messages.*',
]

v3TraitPaths = [
  '$.operations.*',
  '$.operations.*.channel.messages.*',
  '$.operations.*.messages.*',
  '$.components.operations.*',
  '$.components.operations.*.channel.messages.*',
  '$.components.operations.*.messages.*',
  '$.channels.*.messages.*',
  '$.components.channels.*.messages.*',
  '$.components.messages.*',
]

def apply_traits(input: dict):
    # Get the major version of the AsyncAPI version in use
    version = input['asyncapi'].split('.')[0]
    trait_paths = []
    merge_function = merge_overwrite_obj
    if version == '3': 
        trait_paths = v3TraitPaths
    elif version == '2': 
        trait_paths = v2TraitPaths
        merge_function = merge_keep_obj

    for path in trait_paths:
        jsonpath_expression = parse(path)
        for obj_match in jsonpath_expression.find(input):
            if "traits" in obj_match.value:
                traits = obj_match.value["traits"]
                for trait in traits:
                    merged_obj = merge_function(obj_match.value, trait)
                    obj_match.full_path.update(input, merged_obj)

def merge_overwrite_obj(target, patch):
    is_dictionary = type(target) is dict
    if not is_dictionary:
        return patch
    
    result = dict(target)
    
    for key, value in patch.items():
        result[key] = merge_overwrite_obj(target[key] if key in target else None, value)

    return result

def merge_keep_obj(target, patch):
    is_dictionary = type(target) is dict
    if not is_dictionary:
        if target is not None: 
            return target
        return patch
    
    result = dict(target)
    
    for key, value in patch.items():
        result[key] = merge_keep_obj(target[key] if key in target else None, value)

    return result
