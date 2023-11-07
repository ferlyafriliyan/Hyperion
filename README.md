
-----

<p align="center">
<img src="https://repository-images.githubusercontent.com/499265392/cdeb5cae-691b-49c7-9f65-56fc01d54813", width="500", height="500">
</p>

-----

### <p align="center">💥 Hyperion 💥</p>

<br>
<p align="center"><h1>Hyperion is a Python obfuscator, it using crypting and object serialization so its hard to deobfuscating it.</p></h1>
<br>

## <p align="left">📚・Example・📚</p>

<br>

### Normal
```python3
import os, sys

#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system('clear')
    elif "win" in sys.platform.lower():os.system('cls')

def hello():
    myname = ", I am Ferly Afriliyan ! "
    project = "and I just finished creating a python project to Obfuscate Python3 files which is quite difficult to Reverse"
    print("Hello world", myname)
    print(project)
    
if __name__ == '__main__':
    clear();hello()
    
```

### Obfuscated
```python3
__author__ = 'Ferly Afriliyan'
__madeBy__ = 'Hyperion'
__git__ = 'https://github.com/ferlyafriliyan/Hyperion'

# Obfuscated with Hyperion
import marshal, base64
class Gateway():
    def __init__(self, way: bytes, key: int, **ext) -> None:
        self.way = way
        self.key = key
        self.module__ = ext.get('__module', None)
        self.__globals = ext.get('__globals', None)
        self.__module = ext.get('__module', None)
        self.__interpreter = ext.get('interpreter', None)

    def Pass(self):
        exec(marshal.loads(self.module__.b16decode(self.way)),
             {'__selfObject__': self, '__key__': self.key, '__module': self.module__, '__globals': self.__globals, '__InterpreterObject__': self.__interpreter})
        return self
   
class Interpreter():
    def __init__(self, code: str, layersFunction: bytes, module, globals_, backend: bytes = b'') -> None:
        self.__module = module
        self.layersFunction = layersFunction
        self.__globals = globals_
        self.code = {'bytes': code, 'str': str(code)}
        self.__backend = backend

    def __tunnel(self) -> Gateway:
        return Gateway(self.__backend, 7038, __module=self.__module, __globals=self.__globals, interpreter=self)

    def Run(self) -> None:
        decoder = self.__getobject__()
        gate = self.__tunnel().Pass()
        exec(eval(marshal.loads(decoder),
                  {'__selfObject__': self, '__module': self.__module, '__sr_m': eval(eval('chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(34)+chr(109)+chr(97)+chr(114)+chr(115)+chr(104)+chr(97)+chr(108)+chr(34)+chr(41)')), '__globals': self.__globals, 'gate': gate}),
                  self.__globals)

    def __getobject__(self) -> object:
        func = self.layersFunction
        return self.__module.b64decode(func)
   

if __name__ == '__main__':
    try:
        Interpreter(b'QZZ~{Rz*fmQEWy?QC4h4QB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5;C@R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5;O{R8&exQZYtaQbkryQEWy?QC4h4RWLPSRaIm{S5;C*R8>k+QZZ|JRz*fmQ7}qMQ&wz6QB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEWy?S8GO9QB^TvRaIm{S5;C%R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%R8>k+QZZ|JQbk5iQ7}qMQ&wz6Q7|z>RaIm{S5;C%R8>k+QZPnZQbk5iQEWy?S5!(xQB^TZRxoTzS8GyIR8>k+QZPnZQbtZrQEWy?QdCY=QdKoWRz+k&S8Gy2R8>k?QZZIqQbk5mQ!q|QQC4h4QB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEX&NQdVq5QZO+?RaIm{S5;C%R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%R8>k?QZYtaQbkr$Q!q|QQC4hKQB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEX&LRaR_8QZO}CQ7~jmPDN5eR8>k+QZPj@Rz*fmQEW;`PDXG=QdK!iRaIn4S5;C%RBTFDQZPnZQdLe;RcuB`QC4h4QB^TRRaIm{S5;C%R8>k+QZPnZQbk5jRWM3OQC4tOQB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%RBTFCQZPk%QdLe;RcuB`QdVq5QB^TRRaIm{S5;C%R8>k+QZPnZQbk5jRcuyBQB+D*R8~e)RWN8mS5;C%R8>k+Q$<!<Qbk5iQ*3BRQ&wz7R8=uURWM{iS5;C@RBLcjQZQ?JQblY|QEX&NQfo>@QB^TZRaIm{S5;C%R8>k+QZPnZQbk5iQEWy?QC4h4QdKcSRaInKO>9y^R8~q@QZYtaQbjpZQ!q|QQC4hKQB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEX^RQdVq5QB^TRRaIm{S5;C%R8~q-QZPk&Qblx5QEW~~S5!(xQB^raQEO~US5;C(R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIj#QC3nyR8>k+QZPnZQbk5iQEW~~QC4h4R8=)gRaIn4O)yeQR8>l0Q&n0+Qbk5iQ*1^^QC4h4QB^TRRaIm{S5;C%R8>k+QZPk&R#i?;QEWy?QC4h4QB^TRRaIn4S5;C%RBTFDQZPngQbjROQEWy^Qfo$5QdKcSRcmBIS5;C%R8>k+QZPnZQbk5iQEWy?QC4h4R53<NRaIm{S5;C%R8>k+QZPngQbk5iQEX&LR#t39QdKomR#jv}QEOI2RaQz;QZQCpQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%RBB2?QZPnZQbk5iQEWy?QC4h4QdKcSRaInKO>9y^R8~q@QZYtaQdMM9Q!q|QQC4hKQB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEX^RQdVq5QB^TRRaIm{S5;C%R8~q-QZPk&Qblx5QEW~~S5!(xQC3PsQEO~US5;C(R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIj#QC3nyR8>k+QZPnZQbk5iQEW~~QC4h4R8=)gRaIn4O)yeQR8>w#Q&n0+Qbk5iQ*1^^QC4h4QB^TRRaIm{S5;C%R8>k+QZPk&R#i?;QEWy?QC4h4QB^TRRaIn4S5;C%RBTFDQZPngQbjROQEWy^S8GOAQdKcSRcmBIS5;C%R8>k+QZPnZQbk5iQEWy?QC4h4R53<NRaIm{S5;C%R8>k+QZPngQbk5iQEX&LR#t39QdKomR#jw1S5;O-RaQz;QZQCpQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%RBB2?QZPnZQbk5iQEWy?QC4h4QdKcSRaInKO>9y^R8~q@QZYtaRz*%yQ!q|QQC4hKQB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEX^RQdVq5QB^TRRaIm{S5;C%R8~q-QZPk&Qblx5QEW~~S5!(xQ7|!7QEO~US5;C(R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIj#QC3nyR8>k+QZPnZQbk5iQEW~~QC4h4R8=)gRaIn4O)yeQR8>w!Q&n0+Qbk5iQ*1^^QC4h4QB^TRRaIm{S5;C%R8>k+QZPk&R#i?;QEWy?QC4h4QB^TRRaIn4S5;C%RBTFDQZPngQbjROQEW;`RBJ|7QdKcSRcmBIS5;C%R8>k+QZPnZQbk5iQEWy?QC4h4R53<NRaIm{S5;C%R8>k+QZPngQbk5iQEX&LR#t39QdKomR#jw1S5;O-RaQz;QZQCpQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%RBB2?QZPnZQbk5iQEWy?QC4h4QdKcSRaInKO>9y^R8~q@QZYtaRz+-5Q!q|QQC4hKQB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEX^RQdVq5QB^TRRaIm{S5;C%R8~q-QZPk&Qblx5QEW~~S5!(xQ7|=3QEO~US5;C(R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIj#QC3nyR8>k+QZPnZQbk5iQEW~~QC4h4R8=)gRaIn4O)yeQR8??TQ&n0+Qbk5iQ*1^^QC4h4QB^TRRaIm{S5;C%R8>k+QZPk&R#i?;QEWy?QC4h4QB^TRRaIn4S5;C%RBTFDQZPngQbjROQEWy^R%=F9QdKcSRcmBIS5;C%R8>k+QZPnZQbk5iQEWy?QC4h4R53<NRaIm{S5;C%R8>k+QZPngQbk5iQEX&LR#t39QdKomR#jw1O)*wPRaQz;QZQCpQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%RBB2?QZPnZQbk5iQEWy?QC4h4QdKcSRaInKO>9y^R8~q@QZYtaRz+4)Q!q|QQC4hKQB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEX^RQdVq5QB^TRRaIm{S5;C%R8~q-QZPk&Qblx5QEW~~S5!(xQ7}0~QEO~US5;C(R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIj#QC3nyR8>k+QZPnZQbk5iQEW~~QC4h4R8=)gRaIn4O)yeQR8??cQ&n0+Qbk5iQ*1^^QC4h4QB^TRRaIm{S5;C%R8>k+QZPk&R#i?;QEWy?QC4h4QB^TRRaIn4S5;C%RBTFDQZPngRz*fmRcuB`QB+PvQ!p_@R#jwLO>0s_RaJCDQ&ntQQbkTqQEWy?QC4h4QB^TRRaIm{S5;C%R8>k+QZaBsRz*fqQ*1^^QC4h4QB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaInRQC3nyRclI8QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEWy?S5!(>QB^c~QEO~US5;C(R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaInKO>0s_RaQz^QZYtaR#jwDQ!r9UQfp2|Q87kSRaIn8S5;C%R8>k+QZPnZQbk5iQEWy?QC4h4QB^fmQEOyIS5{I&R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%R8>k+QZPnZQbk5mQ!q|QQC4h4QB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEX^PS5|CAQB^fzRz+k+S5;C%R8~q-QZPk&Qblx5QEYHXS5!(xQ87wPQEO~US5;C(R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5{I&R8>k+QZQ^<Qbk5jRcu;FQENt3R8=)YRcmZvQC3z)R8>k-QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%R8??NQZPnZQbkryQEWy?S5!(>QC3D%Rxo5zS8Gy2RBTFCQZQ^<Rz)#SQEW~~Q&dhxRWLC_RcmZVQEO5{R8~q-QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5;C(R8>k+QhHG^Rz+4$S8Ps6QdV$9Q&vhuQEOyFQC3n+RcuOEQ&wwwQbkTrS8Q5HPDDyYR8=`cRxoT@O)*kNRBLodQZZUZQbjpZQ*1^`S5!(xR8=)oR%>H0S8GyERaS6WQ$<!`Qbk5jQEW;`S5!_#R4_49RxoHrO)yqSRBTFNQhHG^Rz)#RQ*2~PR%=d1Q7|z?QEOyZQbkfsRcuOFQ&vTKQbkTrRcuyBS5!(>Q&lljS4C(>O>9<9RBLodQ&vhsRz*foQEXO8QB+P<RWLPSRaInKO>9z7R8~q@Q$<yJQdKceRWMpgRcl67QB^fzR%>ipO>9<9RBTFFQZZ{VRz*2aQEXaDS5!(?R8=&2QEOyNQC3n;R4__eQZYq(Rz+-2S8PT|PDXH5QZYtLRWNK?S8G;IRBTFFQZZ{VRz*2aQEX&MQB+P<Q!q7CRWM{rQ87|ZR90|UQ&wwwQdMkDRWM{oS5!_#R8=)gS4Ct>O)yqSRBUizQZZ~=Rz)#SRcvTTQ&dhxRWLPFQblB1PDWBtR4{N@QZQ9|QdM+LRWM{oRa8<%R4_S9S4Ct(O)yeSRBUimQZZ{VRz)#WRcvHRR%=dGRWLO~QZQsfS5;C%R8>k+QZPzHRz^-wRcua3QC4h4QB^TRRaIm|Q87|fRBTFEQZPnZQbk5iQEWy?QEN_BRWLPSR%>KJS5;C%R8>k+QZPzHRz^-wS8P&9QC4h4QB^TRRaIm|Q87|fRBTFBQZPnZQbk5iQEWy?QEN_BRWLPERcmBIS5;C%R8>k+QZPzHRz^-wS8P^DQC4h4QB^TRRaIm|Q87|fRBTFDQZPnZQbk5iQEWy?QEN_BRWLPER#jv|S5;C%R8>k+QZPzHRz^-vRcuB`QC4h4QB^TRRaIm|Q87|fRBUirQZPnZQbk5iQEWy?QEN_BRWLPES8HTKS5;C%R8>k+QZPzHRz^-wRcvfXQC4h4QB^TRRaIm|Q87|fRBK9FQZPnZQbk5iQEWy?QEN_BRWLPSS8HTKS5;C%R8>k+QZPzHRz^-wS8PT|QC4h4QB^TRRaIm|Q87|fRBUimQZPnZQbk5iQEWy?QEN_BRWLPFQZQsfS5;C%R8>k+QZPzHRz^-wRWMpeQC4h4QB^TRRaIm|Q7~3SR8>k;QZaBvQbjpVO>0(4QdVq5Q7|=ORWM^QQC3nyRBLcqQZZF}Rz+-2RcvHPQ)^B|QZP9~RWN8qS5;C(RclT|QZPj@QbjROQ*2~PR#Z+!QZO}CQZQs%O>0t4R4{N@Q&v@aQbjpWO>0U>Q&dt#Q&lxXRxoT@O)yqWR8~q^QhHH&QbkryQEX^PRa8z@QdKo!S8HTSS5;C_RBK9DQ&wzYQbk5jS8P&9S8GZ|R8=`kRxo5zS8Gy2RBK9FQhHG^Rz*2ZQEX&LR#Z+^QdKomS8HTpQbkfuRcmlmQZPk&QdKceRcua3S5!_#R4_G5S4Ct_O)yeORBTF9QhHH&QbjRPQ*2~PS5!_$Q!p`8RaIn4S5{U`R4{N-QZPnZQbk5iQEWy?QC4h4R8=udQblA=S5;C(R8>k+QZPnZQbjRPQ*2~PRa8z@QB^fmQZQpMS8GyGRBK99QZPk&QdKceS8P&9Q)^09QdKcSS4Ct_O)*kbRBUinQZPzFRz*fqQ*2I1R90|CQ&llkQdMM6Q87|RR8>k=QZO)jQdMM6Rcu;FS5|CQR4_49RWM{iO>9z1RBTFDQhHKhQbjRSQEX&MQdCYxQ!q7CRcmBnQEXB|RaJ0UQZYq(Qblx6RcvHPQ&wz6R8=uyRxoT%O)yeSRBTF9QhHKhQbkr!QEX00QdV$QQ7|z?QEOyMS5;C*R8>k;QZPngQbk5jRcvrbS5!_#QdKcSRWM{qO)yqSRBTFNQZaBuRz*2aQ*3BSQC4t8QdKciRaInKPDWBrRcmlmQZPk&Rz+k_S8Q-dPDXH5QdUY!S4Ct(O)yqSRBTF9QhHH&QbjRORcvHRS5!__QdKonQdMM2Q87|ZRaS6VQ&wwwRz*2aRcu;FPDXG=QdK!aRWN8qS8P^9RBTR2QhHKhRz+4*Q*3BRR8&q?RWLPSRz+hlO>0t4RBLcpQ&vV{QbtBjRcvTTS5|OUR8~e|Rxo5%O)yeKRBUimQZQ?JRz+4&Q*1^`QdV$9QB^ThRaIn4S5;C*R8>k?QZZF}QdMM6RcvrbS5!_#QdKcSRWM{qO)*kXRBTFNQZaBuRz+4$Rcua3QB+PvRWLPFQfp*NS5;C_R90|VQ$<yJRz+k^RWMpePDX4+R8~e|Rxo5nO)*kRRBTFEQZaBvQbjpVRcvHRRaS6DQ!q7DQblB8QbkfwRBUiqQZZF}Rz+4$RcvfXQ&dt_QZYtLRxoT@O)*kPR8~$$QhHKhRz*2bQ*3BRR8&q?Q&lxnR%>KoQ7}?QR4__ZQhHH(QblA>RWMRWPDXH5QdKo!RWN8qS5;O-R8>wxQZZ|JQbjROQ*2~NS5|OEQB^flS5;(MO>9z5RaS6VQ&li}QdKcdRcvfXQ&dt_QZYtLRaI<8S8Gy2R8~q-QZQ^<QbkryQEX&NRa8z@RWLPFQfp*dS5{I^RclIEQZZIxQbk5iO>0(2Q&wz6QdKciRWNK$S8Gy2RBK9MQZQ^<QbjRNQ*2~PRaS6CQB^fVRxo5*O>9z7R8~q@Q&li}Rz^-vRcuB`RaR_OR8=)oS4Ct>O)yeaRBTQ~QZZ{VRz*2bQ*2~NQdCYxQ!p`8RaIn4S5{I+R8>k;QZQ^<QdLe)RcuB`Q&wz6QdKcSRWM{iO)*kJRBUimQZaBvQbjRRQ*2~NR#Z+!QZO}PR#jw5S5;C-RclIAQZPngQbkrzRcuN~S8GmHR8=)YRWM{iO>0tAR8~q-QZaBsRz*2aQ*3BRR8&q?Q&lljRaInKO)yeUR4{N@Q&v@aQbtZsS8P&9S5#6(R8=)gRxo5zS8Gy2RBTFBQhHKhQbjROQ*2~NQdCY=Q&lxnS8HTpQ87|ZRBUimQZPk&QbkTqRcuB`PDX4+R4_S9S4Ct}O)yeYRBTR2QZaBuRz+4$QEX^PQB+P<QdKonQZQs;QC3n;RBLcpQZO)jRz+-1RcuB`PDDyYR8~q;RWM{iO>0(8RBTFAQZZ|KQbjpWQ*3BRR8&qyQZO}BRcm7~O>0t4RBLclQZPk%Rz*fnS8Q-dPDDyYR8=`cRxoT@O)yqWR90|RQZQ^<QbjRORcvHQQdCYxQZO}BR%>H0S8P&7R8>k@QhHH(QbtBkRcvrbS5|OUR8=`cRWM{iO)yeaRBUinQZQ^<QbjpVQ*3BRR#Z+!RWLPSR#jwLO>9y|R8>k?QZYq(QbtZsRcvHPS5!_#R8=`kRxo5vO)*kTRBTQ~QhHH&QbkryQEX^PRa8z!R8=ukRaInGS8GyERBLcqQZZ|KQblx6S8Ps5PDXH5R8=)gRWM{qS5;O-R8~q-QZQ^<QbkryQEW~~QB+P<QB^fzRWM{)PDWBrRcmlrQZYthQbtBjRcua3Ra8<%R8=)gRxoT%O)yqSRBTR2QZQ^<QbjpWS8QZTS5!__QdKonQblB1O>0s{R8~q<Q&llxQbk5jRWMdaPDD~wR8~q$Rxo5nO)yqURBTFDQZQ>URz*fqQ*2I1QC4t8QB^ThRaIn4S5;C_R8>k@QZQ?JQbtZsRWMpePDDyYQdK!aS4Ct(O)*kNRBTR2QZaBsRz)#SQ*2~NR8&q?Q&lljS8HTLQC3n$R8>k;QZPngQbk5iRcuB`QENt3R8=`kRxo5*S8Gy2RBLodQZZUZQbjRSQ*2~NQdCYxQ&lxnR%>KeQbkfsRcuOBQZPngR#j|HO>0(2Q&wz6QdKo!R%>ipO>9<9RBTR0QZZ~=Rz)#TQ*2~PR#Zw>R8=)hQZQsnO)*kPRaJ0OQ&m=BQbk5iRcuB`Q&wz6QdKcSRxo5vO)yqSRBTFDQZZ~=Rz*2ZRcua4QC4t8RWLAlQ7~j$PDN5qRBLcpQ&li}QdMM6RWM{oQ&dt#QdK!iRaI<8S8Gy2R8~q-QZQ^<QbkryQ7~3YQdVq5RaG@iQZQs!QbkfuRcmlqQZQ9|QdMkERcu;FR%=p4Q!z?ZQdMk5S5;C{RBLodQZZUZQbjRSQEX&LQdCYwRWLPFQfp*aQbkfsRcuODQ&v`CQbtZrQ7}?URcl67QB^fzRxo2QO)yqSRBTR2QZZ~{QbjRNQ*2~PR8&q?QZY(IQEOyES8P&FRBUiqQZZF}Rz+-6Q7}qKQC4tOR8=uyRxoHnO)*kNRclT|QZPk%QbjRSRcvTTQB+PvQ!q7DQfq8eQC3nyRaJ0TQ&wwvR#h=iRcvrbS8Gm1R4_3^RxoT@O)*kNRBUioQZZUZQblxARWMdcQdVq5Q&lx#RaInKS5{I`RBK9DQ$<QdQdLe)QEX^PS5|CQR8=ukS4Ct_O)*kJRBTF9QhHH&QbjRPQ7~3YQdVq5RaG@iQZQs!QbkfuRBTFEQ$<yJQdMM6Rcu;FR%=p4Q!z?ZQdMk5S5;C<RBUimQZZ|JRz)#RQ*2~NRclU0Q7|z>R%>KhPDWBrRcmlrQZPk&Rz-AAS8P^FRcl67QB^fVRxo5%O)*kZRBTFNQhHH&QdMkHQ*1^^Ra8zzQ!q7QS5;(MO>9z5R8&esQ$<!<Qbk5nRcum7QC4h4QB^TRRaIm{S5;C%RBUimQZPngRz*fmQEWy?QC4h4QC3P+QEOyEPDN5kRaS6VQ&vTKQdKceRcuyBPDDyoR8~e|Rxo5%S8P^HRBUimQZR5tQbk5iQEWy?QC4h4QB^TRRcmBIS5;C%R8>k+QZPk&Rz+k|Rcua3QC4tOQB^TRRaIm|QbkfiR8>k<QZPnZRz*fmQ*1^^Qfp2{RWLC_S5;&~QbkfyRaQz;Q$<xUQdKcdQ7~3XQB+b@QC3PrS8HTKO)yqSRclIBQZPj@QbkryO>0(2QC4t8R4_4NS5<6MS8P&3R4__aQ$<QcQbtZsQ*3BTQ)@~^Q!qJ9Q7~*;O>9<5RaQ!2QZZUYQdMM7QEXC5RBKK}QZO)iQdMMDPDNHqR8>k>Q&li}QbjRSQEXC3RBKK}R8=)pQdML|O)yqQRBUimQ&vV{Rz)#VRcvTTRclT~R4_GEQ7~gLPDNHqR8??TQ&nqvRz^lsRcuB`QC4h4QB^TRS4C__S5;C(RBK9AQZPngQdKcdS8PT|QC4h4QB^fmQblA!S5{I=RBK97QZR5uQbk5iQEWy?QC4h4Q&l-bRaIn4O)*kRR8>k;Q&wzYRz*fmQEWy?QB+PwQZO+?Rcm7~O>0s@R8~$%QZQCpQbk5iQEWy?RaS6SQB^TvR#jwLS5;C-RcuO9QZPnZQbk5iQEXO7PDX4+QZO|`S8HTKS8P^JR90|OQZPnZQbk5jQEXC3QC4tOQ&vVxRaIn9QbkfkR8>k+QZPnZQblZ2QEWy?R8&e;QB^TRRz+-DS5;C%R8>k+QZPk%Rz*%uQEXC3R#tFTQB^Q`QZQsrS5;C%R8>k+QZY(IQbk5iS8Q5HRaR_8QZY(XRcmBIS5;C%R8>k=QZO-EQblA>Q*2g9QC4tPR8=ucRaIm{S5;C%RBLcqQZPngRz-ADQ*1^^RBKX2QB^TRRaIm{S5;C>RaQz;QZO)iR#kLPQEXC5S5|OUQB^TRRaIm{O>9z7R8>k<QZZUZQbk5iO>1OGQdVq5QB^TRRaInCS8P&3R90|TQ&wzRQblA_RcuN~QC4h4QB^TRRxo5rS5;C-RBTFDQZPngR#h=hQEWy?QC4h4QB^flRxo5jS8P&FR4{N-QZO||QblA=QEWy?QC4h4R8=ukRaIn8O)yqOR8>k<Q&wzRRz*fmQEWy?QB+DrQZO+?Rz+lCQC3nyR8&exQZQCpQbk5iQEWy?S8Gm1QB^TvS4Ct(S5;C-RcuO9QZPnZQbk5iQEX^PQdVq5QZO}PR#jv|S8P^JR90|OQZPnZQbk5jRWMdaQC4tOR4_G5RaIn9QbkfkR8>k+QZPnZQblY|S8PT|R8&q?Q!p_@Rz+-DS5{I&R8>k+QZPk&Rz^lnQEXC3PE|@pQB^Q`QZQsfS5;C%R8>k+QhHWHRz*fmS8QlXR#t39QZY(XRz+k&S5;C%R8>k@Q$<EvQblA>O>1OGQC4tPR8=ucRaIm{S5;C%RBK9AQZPngRz*2eRcuB`RBKX2Q7|z>RaIm{S5;C<R8~q-QZYq&Qblx5QEXO9S5|CAQB^TRRaIm{O>0t4R8>k=QZYp^Qbk5jQ7~jkR90+7QB^TRRaInCS8Gy2RBK9BQ$<!<QblZ2RcuN~QC4h4QB^TRR#jw9S5;C-RBK9MQZPk%QdKcdQ*1^^QC4h4QB^fWQblA!O>0t0RcuO9QZY(JQbk5iQEWy?QC4h4Q!p_@RaInCO>9y~R8>k=Q&wzYRz*fmQEWy?QB+DsQZO+?R#jwHO>0s@RBKL1QZQCpQbk5iQEWy?RaS6SQB^TvR%>KZS5;C<RcuOAQZPnZQbk5iQEXaBPDX4+Q&lxgQEOyEO>0(8R8>k+QZPnZQbk5jQ!q|QQB+DrQ!z?QRaInDQbkfoR8>k+QZPnZQblx6S8PT|Ra8n=R8=uUR#j|TS5{I&R8>k+QZPk%QblA=QEXC3R%=p4QB^fWQZQsjS5;C%R8>k+QZZ~{Qbk5jQEX&LR#t39Q&vh-RaIm{S5;C%R8>k?QZZ~=QblY}RcvrbQB+DsR8=uyRaIm{S5;C%RBTFAQZPk%QbjRRQ*1^^Rclg3Q7|z>RaIm{S5;C<R90|OQZO)jQdLe)QEXO9S5|CQQB^TRRaIm{O)yqUR8>k=QhHKaQbk5jQ7~jkQC4h4QB^TRRaIj!S5{I&RBK9EQZO-EQblZ2Rcum7QC4h4QB^TRRxoT*S5;C<RBUioQZPk%QdKcdQ*1^^QC4h4QB^fVRz+k&S8P&HRBK97QZY(JQbkTqQEWy?QC4h4R4_GRRaInCO)*wPR8>k=Q&wzRQbk5iQEWy?QB+P=QdKcSR#js$Q87|NRBKL1QZO-EQbk5iQEWy?PDD;sQB^fVS4C`ES5;C<RcuOAQZPnZQbk5iQEXO7R90+7QZO`mQZQsfO>0(8R8??NQZPnZQbk5jQEW~~QB+D*Q&lxfRaInHQbkfiR8>k+QZPnZQblY}RcuB`R#ZwwRWLC_R%>ipS8P&3R8>k+QZPk%QbkryQEXaBRcl67QB^feQZQsjS5;C%R8>k+QZYthRz*fmS8P^FQdVq5Q!z?YRcmBIS5;C%R8>k=Q&vV=Qblx6Q*1^^QB+D+R8=uURaIm{S5;C%RBLckQZPk%Rz-AAQEWy?R%=p4QZO+?RaIm{S5;C<RclI8QZZF|Rz-A9QEXaDS5|CQQB^TRRaIm{O>0s}R8>k<QZZF|Rz*fnQ!r#mQdVq5QB^TRRaInGPDN5eRBLcoQ&ntQQblxARcuB`QC4h4QB^TRR%>idS5;C>RBLodQZPk%R#h=hS8PT|QC4h4QB^fdS5;&}O>9z5R8>k+QZZUZQbkTqQEWy?QC4h4Q&llxRaIn8O)yeIR8>k>Q&wzRRz*fmQEWy?QB+PvQZO+?R%>KhO)yeIRBLodQZPnZQbk5iQEWy?S5!__QB^fdRxoHrS5;C>RcuOCQZPnZQbk5iQEX&LR90+7Q!q7DQEOyEO>9<9R8??NQZPnZQbk5jQEXC3QC4tOR8~eyRaInHQbkfkR8>k+QZPnZQbjRSQEWy?R#Z+^QB^TRR%>ipS5;C%R8>k+QZPk&Rz*%uQEXaBPDXH5QB^feQZQsrS5;C%R8>k+QZaBuQbk5jQ*3BRRaR_8Q!z?YRcmBIS5;C%R8>k=QZO-EQblA>S8P^DQB+D+R8=ucRaIm{S5;C%RBUirQZPk%Rz*2dQ*1^^R%=p4QB^TRRaIm{S5;C_RaQz;QZZF}R#kLPQEXaDS5|OUQB^TRRaIm{O)*kXR8>k>QhHWJQbk5jQ!r#mQdVq5QB^TRRaInCS8P&3R90|VQ&wzRQblxARcuN~QC4h4QB^TRR#jw5S5;C@RBK9CQZPk&QdKcdQEWy?QC4h4QB^fVRxo5jO)yeQR4{N-QZaBvQblA=QEWy?QC4h4Q&lljRaInKO>0&}R8>k?Q&wzRRz*fmQEWy?QB+DrQZO+?Rz+k}QC3nyRBTR2QZQCpQbk5iQEWy?RclT~QB^flR%>KJS5;C@RcuO9QZPnZQbk5iQEXaBQdVq5R8=)gR#jv|O)yqYR90|OQZPnZQbk5jQ7~3WQB+PvQ!q74RaInRQbkfkR8>k+QZPnZQblY|S8PT|R8&e;Q!p_@RxoT@S5{I&R8>k+QZPk%Rz^lnQEX&LR%=Q{QB^fmQZQsfS5;C%R8>k+QZZUXRz*fnRcu;HS5|CAR8~q;Rz+k&S5;C%R8>k>Q$<EvQbjRORcuB`QB+PwR8=ucRaIm{S5;C%RBK9AQZPngRz)#RQEWy?S8Gy5Q7|z>RaIm{S5;C@R90|OQZZ|KQbjRNQEX&NS5|CAQB^TRRaIm{O)yeWR8>k?QZaBsRz*fnRWM{oR90+7QB^TRRaInKS8P&3RBTFEQ&ntQQbjRSRcuN~QC4h4QB^TRR#jw9S5;C-RBTQ}QZPk&QdKcdQ*1^^QC4h4QB^fmQfp*FO)yeWR8??NQZaBvQbk5iQEWy?QC4h4R4_49RaInKO)*kTR8>k?Q&wzYRz*fmQEWy?QB+PwQ!p_@Rxo2QO)yeIRBTR2QZQCpQbk5iQEWy?RaS6SQB^TvS4Cu6S5;C@RcuOAQZPnZQbk5iQEX^QQdVq5R8=&2QblA!O)yqYR8>k+QZPnZQbk5jO>0(2QB+PvQ&llTRaIj#QbkfoR8>k+QZPnZQbjpXQ*1^^S5!(xQ7|z>S4C`ES5{I&R8>k+QZPk%QblA=QEXC3RaR_OQB^c~QZQsjS5;C%R8>k+QZYq(Qbk5jS8P^FQdVq5R540ZRcmBIS5;C%R8>k=Q&ntQQbjpWQ*2sDQB+P=R8=uURaIm{S5;C%RBLcpQZPk&Rz-ADQ*1^^PE}GxQZO+?RaIm{S5;C<RaQz;QhHH&R#jF`QEX^RS5!__QB^TRRaIm{O>0(0R8>k@QZZ~=Qbk5jO>1OGQdVq5QB^TRRaInDQEO5{RBUiqQZPnZQbjpaRcvTTQC4h4QB^TRR#j|DS5;C_RBTFGQZPk&R#h=hQ*1^^QC4h4QB^fWQ7~jeO)*kVR4__XQhHWJQbk5iQEWy?QC4h4R8=`kRaIj!O)*kLR8>k@Q&wzYRz*fmQEWy?QB+DsQdKcSS4CqmS8Gy2RBB2{QZPnZQbk5iQEWy?PDDyYQB^fzS4CqmS5;C_RcuO9QZPnZQbk5iQEXO7RaR_8RaG@aQ7~jePDNHuRBK97QZPnZQbk5jQEX&LQB+P<Q&vV{RaIz1QbkfwR8>k+QZPnZQblY}RcuB`PDDyoQ7|z>S5<6US5{I&R8>k+QZPk%QbjRNQEX^PR#t3PQB^raQZQsrS5;C%R8>k+QZYq(Qbk5jS8Q5HR90+7RaQz<RcmBIS5;C%R8>k@Q$<!<QbkrzQ*2U5QB+b!R8=ucRaIm{S5;C%RBLcqQZPj@Qblx9S8PT}QEO5~QB^TRRaIm{S5;C>RclI8Q$<C2QbjpVQEYHZS5!(xQB^TRRaIm{O>9z7R8>k^QZYp^Qbk5kQ!r#mQdVq5QB^TRRaInCPDWBfR4{N>Q&vV=QbtZwRcuB`QC4h4QB^TRR#j|PS5;C}RBKL1QZPj@R#h=iQEWy?QC4h4QB^fVS8HTKPDWBpR8>k+Q$<=tQbtZrQEWy?QB+DsR8=uURaIm{S5;C%R8>k?QZZ~=Qbk5jO>1OGQC4h4QB^TRRaInKS8P&3RBUiqQ&vV=QbjpaRcuB`QC4h4QB^TRRxoT@S5;C_RBUizQZPk&R#h=hQEWy?QC4h4QB^flRWM{iO)*kXRaJ0OQhHWJQblx5QEWy?QC4h4QB^TZS4C_}S5;C_RBUimQZR5sRz*fmQEWy?QC4h4QB*KFP*FWS',
            b'4wAAAAAAAAAAAAAAAAMAAAADAAAA82YBAACXAHQBAAAAAAAAAACrAAAAAAAAAGQBGQAAAH0AdAEAAAAAAAAAAKsAAAAAAAAAagMAAAAAAAAAAAAAAAAAAAAAAABkAqsBAAAAAAAAcwF5AHQBAAAAAAAAAACrAAAAAAAAAGQDGQAAAH0BdAEAAAAAAAAAAKsAAAAAAAAAZAQZAAAAfQJ8AWoEAAAAAAAAAAAAAAAAAAAAAAAAZAUZAAAAfQN8AmoHAAAAAAAAAAAAAAAAAAAAAAAAfAOrAQAAAAAAAH0DfAJqCQAAAAAAAAAAAAAAAAAAAAAAAHwDqwEAAAAAAAB9A3wCagsAAAAAAAAAAAAAAAAAAAAAAAB8A6sBAAAAAAAAfQN8AmoNAAAAAAAAAAAAAAAAAAAAAAAAfAOrAQAAAAAAAH0DdAEAAAAAAAAAAKsAAAAAAAAAZAYZAAAAag8AAAAAAAAAAAAAAAAAAAAAAAB8A6sBAAAAAAAAfQN8A1MAKQdO2glfX2dsb2JhbHPaBGdhdGXaDl9fc2VsZk9iamVjdF9f2ghfX21vZHVsZdoFYnl0ZXPaBl9fc3JfbSkI2gdnbG9iYWxz2gNnZXTaBGNvZGXaCWI4NWRlY29kZdoJYjY0ZGVjb2Rl2gliMzJkZWNvZGXaCWIxNmRlY29kZdoFbG9hZHMpBNoIX2dsb2JhbHPaA29iatoGbW9kdWxlcgoAAABzBAAAACAgICD6CDxzdHJpbmc+2gxSZW1vdmVMYXllcnP6FUh5cGVyaW9uLlJlbW92ZUxheWVyc2EAAABzogAAAIAA3BMakzmYW9ETKYgI3A8Wi3mPfYl9mFbUDyTYDBLcDhWLadAYKNEOKYgD3BEYkxmYOtERJogG2A8Sj3iJeJgH0Q8giATYDxXXDx/RDx+gBNMPJYgE2A8V1w8f0Q8foATTDyWIBNgPFdcPH9EPH6AE0w8liATYDxXXDx/RDx+gBNMPJYgE3A8Wi3mYGNEPItcPKNEPKKgU0w8uiATYDxOIC/MAAAAA',
            eval(eval('chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(34)+chr(98)+chr(97)+chr(115)+chr(101)+chr(54)+chr(52)+chr(34)+chr(41)')), globals(),
            b'E30000000000000000000000000200000003000000F390000000970074010000000000000000AB000000000000006401190000007D0074010000000000000000AB000000000000006402190000007D0174010000000000000000AB000000000000006403190000007D027C016A020000000000000000000000000000000000006404190000007D0364057C005F0200000000000000007C0264067A05000064077A0B00007C036602530029084EDA0E5F5F73656C664F626A6563745F5FDA155F5F496E7465727072657465724F626A6563745F5FDA075F5F6B65795F5FDA05627974657354E908000000E7000000000000F83F2903DA07676C6F62616C73DA04636F6465DA0865786563757465642904DA036F626ADA0E696E7465727072657465724F626ADA036B65797209000000730400000020202020FA083C737472696E673EDA0747617465776179FA104879706572696F6E2E476174657761792C00000073520000008000DC0E158B69D01828D10E298803DC19209B19D0233AD1193B880EDC0E158B699809D10E228803D80F1DD70F22D10F22A037D10F2B8804D8171B88038C0CD81114907191179833911DA014D00F26D00826F300000000'
        ).Run()
    except (KeyboardInterrupt, Exception) as e:
        exit(f"[Error] {str(e).capitalize()}!")
# Lu Kontool
```
## - Run a Termux :
```python
$ termux-setup-storage
$ termux-change-repo
$ pkg update && pkg upgrade -y
$ pkg install git
$ pkg install python -y
$ pkg install python-pip
$ git clone https://github.com/ferlyafriliyan/Hyperion
$ cd Hyperion
$ pip3 install -U -r requirements.txt
$ python Run.py
```


<br>

## <p align="left">📢・Informations・📢</p>
- `✅` Code can be compiled with marshal and eval.
- `✅` The code cannot be compiled with the code itself
- `⏹` Confusion Duration on the input file is quite long
<br>

## <p align="left">⭐・Repository・⭐</p>
If you like this repository, **star it** ! And if you want to share your opinion, please go to the **repository discussion**. 

<br>

-----

<p align="center"><strong>By Ferly Afriliyan : <a href="https://github.com/ferlyafriliyan/">github.com/ferlyafriliyan</a></strong></p>
