#Etmen ve Cevre Sınıflarını Tanımlayın

from mesa import Agent, Model
from mesa.time import RandomActivation
import random
import matplotlib.pyplot as plt

class Etmen(Agent):
    """Başlangıç varlık değerine sahip bir etmen."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.varlik = 1

    def step(self):
        # Etmenin her adımda gerçekleştireceği eylem
        print("Merhaba, ben etmen " + str(self.unique_id) + ".")
        if self.varlik > 0:
            baska_etmen = random.choice(self.model.schedule.agents)
            baska_etmen.varlik += 1
            self.varlik -= 1

class Cevre(Model):
    """Etmenlerin yer alacağı çevre."""
    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        # etmenlerin oluşturulması
        for i in range(self.num_agents):
            a = Etmen(i, self)
            self.schedule.add(a)

    def step(self):
        self.schedule.step()

#Modeli Oluşturun ve Çalıştırın

# Rastgele 10 etmen oluşturur
yeni_model = Cevre(10)

# 10 adımlık eylemde bulunması sağlanır
for i in range(10):
    yeni_model.step()
    
#Etmen Varlıklarını Görselleştirin

etmen_varlik = [a.varlik for a in yeni_model.schedule.agents]
plt.hist(etmen_varlik)
plt.title('Etmen Varlık Dağılımı')
plt.xlabel('Varlık')
plt.ylabel('Etmen Sayısı')
plt.show()

#Daha Uzun Bir Simülasyon Çalıştırın ve Görselleştirin

butun_varliklar = []

# 100 adımlık eylemde bulunması sağlanır
for j in range(100):
    yeni_model = Cevre(10)
    for i in range(10):
        yeni_model.step()

    for etmen in yeni_model.schedule.agents:
        butun_varliklar.append(etmen.varlik)

# Etmen hareketlerinin görselleştirilmesi
plt.hist(butun_varliklar, bins=range(max(butun_varliklar)+1))
plt.title('Uzun Simülasyon Etmen Varlık Dağılımı')
plt.xlabel('Varlık')
plt.ylabel('Etmen Sayısı')
plt.show()














