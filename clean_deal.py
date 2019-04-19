def clean_deal(input_text):
    x = re.sub("/","",input_text)
    x = re.sub("\|","",x)
    print(x)
    x = re.sub("\+","",x)
    #print(x)
    
    x = re.sub(r'[a-zA-Z0-9\$]+([0-9\.]+)[a-zA-Z0-9\%]+',"",x)
    
    digits = ['one','two','three','four','five','six','seven','eight','nine','ten']
    for d in digits:
        x = re.sub(d,"",x)

    x = re.sub(r'\[(.*?)\]', "", x)
    x = re.sub(r'\((.*?)\)', "", x)
    #print(x)
    
    x = re.sub("[Ss]ave up to","",x)
    x = re.sub("[Cc]ash [Vv]oucher[s]?","",x)
    x = re.sub("[Vv]oucher[s]?","",x)
    x = re.sub("[Dd]iscount[s]?","",x)
    x = re.sub("[Ss]ave","",x)
    x = re.sub("[Pp]erson[s]?","",x)
    x = re.sub("of "," ",x)
    #print(x)
    
    x = re.sub("[Aa]nd ","",x)
    x = re.sub("for ","",x)
    x = re.sub("[Oo]r ","",x)
    x = re.sub("with ","",x)
    x = re.sub("for ","",x)
    x = re.sub("at ","",x)
    x = re.sub("\@","",x)
    
    x = re.sub(r'([0-9]+)'," ",x)
    #print(x)
    
    print(x)