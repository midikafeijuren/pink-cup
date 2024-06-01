#made in china
#by midikafeijuren
def pkp_jm(main_nr = "",jmdj = "1"):
    from cryptography.fernet import Fernet
 
# 生成一个密钥
    
    back_list = []
    
    
    #Code Time
    from datetime import datetime
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year
    main_nr_list = list(main_nr)
    return_lest = []
    for unkdm_evry in main_nr_list:
        return_text = ''.join(f'\\u{ord(unkdm_evry):04x}')
        return_lest.append(return_text)
    
     
    
        

   

'''
        for aaa in best_small_txt_list:
            if aaa == "/":
                if day % 2 == 1:
                    aaa = "~"
                elif day % 2 == 0:
                    aaa = "`"
            elif aaa == 1:
                if day 
                
'''
    
pkp_jm("时间啊无敌")
