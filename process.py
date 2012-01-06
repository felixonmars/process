from MoinMoin import wikiutil

def execute(pagename, request):
    macro_action = wikiutil.importPlugin(request.cfg, "macro", pagename, "action_" + pagename)
    
    result = macro_action(request)
    
    request.write(result)
    request.close()
