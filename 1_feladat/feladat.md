# Eurovíziós dalfesztivál

Az Eurovíziós Dalfesztivál Európa legnagyobb televíziós könnyűzenei produkciója. Évről évre több tucatnyi résztvevő száll harcba a dicsőségért és a hírnévért, amely a verseny megnyerésével jár. A szabályok egyszerűek: aki a legtöbb pontot kapja az előadására, az nyer. Igen ám, de a pontokat több helyről is be lehet szerezni. Minden ország rangsorolhatja az előadókat, s a rangsorok élén állók kapják a legtöbb pontot.

A verseny pontozási mechanizmusát ismerve írjon programot, amely a standard bemenet soraiból beolvassa azt, hogy az egyes országok melyik előadót hány ponttal jutalmazták! A feldolgozandó sorok alakja a következő:

`ország:előadó:pontszám`

A programja **összegezze az egyes előadók által gyűjtött pontokat**, aztán készítsen egy kimutatást arról, hogy **ki mennyi pontot ért el**! Az előadók az **összpontszámok értékének csökkenő sorrendjében** jelenjenek meg a kimeneten a példa kimenetben látható formában! 
Az összpontszámok mellett **zárójelben tüntesse fel azoknak az előadóknak a számát, akik ennyi pontot értek el**! Ha több előadó is azonos összpontszámot ért volna el, akkor őket **nevük alapján állítsa lexikografikusan növekvő sorrendbe**! 

### Bemenet
```
Norvegia:John Lundvik:8
Magyarorszag:Lake Malawi:12
Norvegia:Lake Malawi:12
Romania:Kate Miller-Heidke:12
Szlovenia:Mahmood:8
Romania:Lake Malawi:8
Norvegia:Tamara Todevska:10
Ciprus:Mahmood:8
Magyarorszag:Tamara Todevska:10
Ciprus:Katerine Duska:12
Szlovenia:Lake Malawi:12
Szlovenia:Chingiz:10
Magyarorszag:ZENA:8
Romania:Chingiz:10
Ciprus:Sergey Lazarev:10
```

## Kimenet
```
44 (1): Lake Malawi
20 (2): Chingiz, Tamara Todevska
16 (1): Mahmood
12 (2): Kate Miller-Heidke, Katerine Duska
10 (1): Sergey Lazarev
8 (2): John Lundvik, ZENA
```