n = 200
wzr =8.65
dcx= 8.75
bttinr= 0.2525
btttrx=0.03232
trx=0
btt=0
cap=1730
p=0
def m(n,cap,p,wzr,dcx,btttrx,bttinr,trx,btt):
    if(cap>100):
        n-=1
        ad = n*dcx
        print("TRX # :",n," |TRXINR:",dcx," |TRX*INR:",ad)
        p += ad-cap
        print("Profit: ",round(p))
        n-=1
        print("TRX # :",n)
        btt = round(n/btttrx)
        print("TRX # :",n," |TRXBTT:",btttrx," |TRX/BTT:",btt)
        sb = btt*bttinr
        print("BTT:",btt," |BTTINR: ",bttinr," |BTT*INR:",sb)
        p =cap-sb
        cap = sb
        print("Cap: ",cap)
        print("P: ",p)
    # m(n,cap,p,wzr,dcx,btttrx,bttinr,trx,btt)

m(n,cap,p,wzr,dcx,btttrx,bttinr,trx,btt)
