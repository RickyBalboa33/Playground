
wzr_trx =8.40
dcx_trx= 8.50
W_bttinr= 0.2640
D_bttinr = 0.27223
btttrx=0.03225
trx=0
btt=0
cap=100
p=0
orders=4
cur_order=0
flag=True
def m(cap,p,wzr_trx,dcx_trx,btttrx,W_bttinr,D_bttinr,trx,btt,flag,orders,cur_order):
    
    if(btt<=0 and flag):
        btt = round(cap/D_bttinr)
        print("BIN # BTT: ",btt)
        trx=round(btt*btttrx)
        print("Bin, Trx #: ",trx)
        # trx-=1
        flag=False
    if(btt<=0 and not flag):
        btt = round(cap/D_bttinr)
        print("DCX # BTT: ",btt)
        trx=round(btt*btttrx)

    if(btt>0):
        print("On DCX, Trx #: ",trx)
        temp_cap= round(trx*dcx_trx)
        print("Cap After TRX sell: ",temp_cap)
        btt=0
        trx=0
        p += (temp_cap-cap)
        print("Profit: ",p," |Cap: ",cap)
    if(orders>cur_order):
        cur_order+=1
        print("++++++++++++++++ Order Number: ",cur_order," +++++++++++++")
        m(cap,p,wzr_trx,dcx_trx,btttrx,W_bttinr,D_bttinr,trx,btt,flag,orders,cur_order)



        
    

m(cap,p,wzr_trx,dcx_trx,btttrx,W_bttinr,D_bttinr,trx,btt,flag,orders,cur_order)
