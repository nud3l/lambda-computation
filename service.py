# -*- coding: utf-8 -*-

def handler(event, context):
    # Your code goes here!
    val1 = int(event.get('val1'))
    val2 = int(event.get('val2'))
    return val1 * val2
