# Feito por Gustavph

print("""                                                                                                                                                                       
    @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                                                                                 
    @@                      @@                                                            
    @@               @@@@@  @@                                                            
    @@               @@@@@  @@                               @@@@@@@@@                             
    @@               @@@@@  @@     @@@@      @@@@@    @@@@@  @@@@@@@@@     @@@     @@  @@@@@@@@  @@@@@@@@  @@@@@    @@@@@                                                       
    @@         @@@@@ @@@@@  @@     @@@@      @@@@@@  @@@@@@  @@@           @@@     @@  @@@       @@        @@@@@@  @@@@@@                                                       
    @@         @@@@@ @@@@@  @@     @@@@      @@@@@@@ @@@@@@  @@@@@@@@@     @@@     @@  @@@       @@@       @@@@@@@ @@@@@@                                                       
    @@  @@@@@  @@@@@ @@@@@  @@     @@@@      @@@@@@@@@@@@@@  @@@@@@@@@     @@@     @@  @@@@@@@@   @@@@@@   @@@@@@@@@@@@@@                                                        
    @@  @@@@@  @@@@@ @@@@@  @@     @@@@      @@@ @@@@@@ @@@  @@@           @@@     @@  @@@            @@@  @@@ @@@@@@ @@@                                                                                                                                             
    @@  @@@@@  @@@@@ @@@@@  @@     @@@@@@@@@ @@@  @@@@  @@@  @@@            @@@   @@@  @@@             @@  @@@  @@@@  @@@                                                                                
    @@  @@@@@  @@@@@ @@@@@  @@     @@@@@@@@@ @@@        @@@  @@@             @@@@@@@   @@@      @@@@@@@@   @@@        @@@   
    @@  @@@@@  @@@@@ @@@@@  @@         
    @@  @@@@@  @@@@  @@@@@  @@        
    @@                      @@     
    @@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                                                            
""")

from moviepy.editor import *
from datetime import datetime
import yfinance as yf

# pegar os vídeos
data = VideoFileClip("data.mp4")
moedas = VideoFileClip("moedas.mp4")
indices = VideoFileClip("índices.mp4")

# Pegar a Data
dia = datetime.now().strftime("%d/%m")

# Formatar a data
textData = TextClip(txt=dia,
                    font="Segoe-UI-Bold",
                    fontsize=48,
                    color="white",
                    method='caption').set_position(("center",490)).set_duration(data.duration)

# Juntar a data com o vídeo e criar o arquivo
datafinal = CompositeVideoClip([data, textData])
datafinal.write_videofile("datafinal.mp4", fps=30)


def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

def get_before_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='2d')
    return todays_data['Close'][0]

def cor_porcetagem(valor):
    if valor > 0:
        colorB = '#7DF983'  # verde
    elif valor < 0:
        colorB = '#FF626C'  # vermelho
    else:
        colorB = "white"
    return colorB

def porcentagem_bolsas(valor,colorB):
    return  TextClip(txt=f"{valor:.2f}%",
            font="Segoe-UI-SemiBold",
            fontsize=40,
            color=colorB
            ).set_duration(indices.duration)


print(get_current_price('^BVSP'))
porcentIBOVESPA = ((get_current_price('^BVSP') / get_before_price('^BVSP') ) -1)*100
print(f"IBOVESPA: {porcentIBOVESPA:.2f}%")

porcentSP = ((get_current_price('^GSPC') / get_before_price('^GSPC') ) -1)*100
print(f"S&P: {porcentSP:.2f}%")

porcentDOW = ((get_current_price('^DJI') / get_before_price('^DJI') ) -1)*100
print(f"DOW: {porcentDOW:.2f}%")

porcentNASDAQ = ((get_current_price('^IXIC') / get_before_price('^IXIC') ) -1)*100
print(f"NASDAQ: {porcentNASDAQ:.2f}%")

porcentDAX = ((get_current_price('^GDAXI') / get_before_price('^GDAXI') ) -1)*100
print(f"DAX: {porcentDAX:.2f}%")

porcentFTSE = ((get_current_price('^FTSE') / get_before_price('^FTSE') ) -1)*100
print(f"FTSE: {porcentFTSE:.2f}%")

porcentSSE = ((get_current_price('000001.SS') / get_before_price('000001.SS') ) -1)*100
print(f"SSE: {porcentSSE:.2f}%")


# Formatar a IBOVESPA número
ibovN = TextClip(txt=f"{get_current_price('^BVSP'):.0f}",
                    font="Segoe-UI-Bold",
                    fontsize=44,
                    align="center",
                    color="white"
                    ).set_duration(indices.duration)

ibovN.save_frame("ibovN.png")
meiaibovespa = ibovN.w/2


coloribov = cor_porcetagem(porcentIBOVESPA)
ibovP = TextClip(txt=f"{porcentIBOVESPA:.2f}%",
            font="Segoe-UI-SemiBold",
            fontsize=44,
            color=coloribov
            ).set_duration(indices.duration)
meiaibov = ibovP.w/2

colorSP = cor_porcetagem(porcentSP)
spP = porcentagem_bolsas(porcentSP,colorSP)
meiaSP = spP.w/2

colorNASDAQ = cor_porcetagem(porcentNASDAQ)
nasdaqP = porcentagem_bolsas(porcentNASDAQ,colorNASDAQ)
meiaND = nasdaqP.w/2

colorFTSE = cor_porcetagem(porcentFTSE)
ftseP = porcentagem_bolsas(porcentFTSE,colorFTSE)
meiaFTSE = ftseP.w/2

colorDOW = cor_porcetagem(porcentDOW)
dowP = porcentagem_bolsas(porcentDOW,colorDOW)
meiaDOW = dowP.w/2

colorDAX = cor_porcetagem(porcentDAX)
daxP = porcentagem_bolsas(porcentDAX,colorDAX)
meiaDAX = daxP.w/2

colorSSE = cor_porcetagem(porcentSSE)
sseP = porcentagem_bolsas(porcentSSE,colorSSE)
meiaSSE = sseP.w/2

# Juntar os índices com o vídeo e criar o arquivo
datafinal = CompositeVideoClip([
    indices,
    ibovP.set_position((145 - meiaibov,176.5)),
    ibovN.set_position((335 - meiaibovespa, 176.5)),
    spP.set_position((150 - meiaSP, 340)),
    nasdaqP.set_position((150 - meiaND, 505)),
    ftseP.set_position((150 - meiaFTSE, 663)),
    dowP.set_position((331.5 - meiaDOW, 340)),
    daxP.set_position((331.5 - meiaDAX, 505)),
    sseP.set_position((331.5 - meiaSSE, 663))
    ])
datafinal.write_videofile("indicefinal.mp4", fps=30)

def get_before_currency(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(prepost='true', interval='1h', period='2d')

    return todays_data['Open'][11]

porcentUSD = ((get_current_price('BRL=X') / get_before_currency('BRL=X') ) -1)*100
print(f"Dólar: {porcentUSD:.2f}%")

porcentEUR = ((get_current_price('EURBRL=X') / get_before_currency('EURBRL=X') ) -1)*100
print(f"Euro: {porcentEUR:.2f}%")

porcentBTC = ((get_current_price('BTC-USD') / yf.Ticker('BTC-USD').history(prepost='true', interval='1h', period='1d')['Open'][0] ) -1)*100
print(f"BTC: {porcentBTC:.2f}%")

# print(get_current_price('BRL=X'))
# print(yf.Ticker('BRL=X').history(prepost='true', interval='1h', period='2d')['Close'][11])
# print(yf.Ticker('BTC-USD').history(prepost='true', interval='1h', period='1d'))
# print(yf.Ticker('BTC-USD').history(prepost='true', interval='1h', period='1d')['Open'][0])

def porcentagem_moedas(valor,colorM):
    return  TextClip(txt=f"{valor:.2f}%",
            font="Segoe-UI-SemiBold",
            fontsize=44,
            color=colorM
            ).set_duration(moedas.duration)

#cores das porcentagens
colorUSD = cor_porcetagem(porcentUSD)
colorEUR = cor_porcetagem(porcentEUR)
colorBTC = cor_porcetagem(porcentBTC)

#formatação para imagem das porcentagens
usdP = porcentagem_moedas(porcentUSD,colorUSD)
eurP = porcentagem_moedas(porcentEUR,colorEUR)
btcP = porcentagem_moedas(porcentBTC,colorBTC)

usdN = TextClip(txt=f"R$ {get_current_price('BRL=X'):.2f}",
                    font="Segoe-UI-Bold",
                    fontsize=44,
                    color="white"
                    ).set_duration(moedas.duration)

eurN = TextClip(txt=f"R$ {get_current_price('EURBRL=X'):.2f}",
                    font="Segoe-UI-Bold",
                    fontsize=44,
                    color="white"
                    ).set_duration(moedas.duration)

btcN = TextClip(txt=f"R$ {get_current_price('BTC-USD')*get_current_price('BRL=X'):.0f}",
                    font="Segoe-UI-Bold",
                    fontsize=36,
                    color="white"
                    ).set_duration(moedas.duration)

usdNW = usdN.w
eurNW = eurN.w
btcNW = btcN.w
btcNH = btcP.h/2 - btcN.h/2

# Juntar as moedas com o vídeo e criar o arquivo
datafinal = CompositeVideoClip([
    moedas,
    usdP.set_position((70, 220)),
    eurP.set_position((70, 410)),
    btcP.set_position((70, 590)),
    usdN.set_position((410 - usdNW, 220)),
    eurN.set_position((410 - eurNW, 410)),
    btcN.set_position((410 - btcNW, 590 + btcNH))
    ])
datafinal.write_videofile("moedasfinal.mp4", fps=30)