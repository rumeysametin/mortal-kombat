import random

def get_player_name(order, other_character): #bu fonksiyonda while true kullanılarak şartları sağlayan isim alana kadar isim isteniyor.
    while True:
        print("------------ {} Kahraman ------------".format(order))
        name = input("Lütfen kahramanınızın adını yazın: ")
        if len(name) < 1:
            print("İsim bölümünü boş bırakmayınız.")       
        elif name in other_character:
            print("{} alındı, lütfen başka bir isim seçin!".format(name))
        else:
            break
    return name

def ask_attack_size():  #bu fonksiyonda saldırı büyüklüğü isteniyor.
    while True:
        attack_size = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin: "))
        if attack_size > 50:
            print("Saldırı büyüklüğü 1 ile 50 arasında olmalıdır!")
        elif attack_size < 1:
            print( "Saldırı büyüklüğü 1 ile 50 arasında olmalıdır!")
        else:
            return attack_size

def attack(power, character):
    probability_of_success = random.randint(0, 100)    #rastgele bir sayı seçiliyor.
    print("--------------- {} Saldırı !! ---------------".format(character))
    attack = ask_attack_size()    
    if probability_of_success > attack:                 #istenen saldırı büyüklüğü rastgele gelen sayıdan küçük olursayki durumu açıklıyor.
        print("{} {} hasar verdi!".format(character, attack))
        power -= attack
    else:
        print("Ooopsy! {} saldırıyı kaçırdı!".format(character))
    return power

def print_result(power1, power2, character1, character2):   #karakter isimleri ve puan değerleri bu fonksiyonla yazdırılıyor.
    print("{}                                                                     {}".format(character1, character2))
    print( "HP [{}]:{}              HP [{}]:{} ".format(power2, (power2//2) * "|", power1, power1//2 * "|"))


def confirm_close():  #tekrar oyun oyna durumunu sorgulayan bir fonksiyon
    while True:
        confirm = input("Bir tur daha oynamak ister misiniz (evet veya hayır)? :")
        if confirm == "hayır":
            print("Oynadığınız için teşekkürler! Tekrar görüşürüz!")
            playing = False 
            break 
        elif confirm == "evet":
            playing = True
            break
    return playing     #evet veya hayır dışında değer girildiğinde tekrar oynamak için sorgulayan satır

def end():
    players_array = []   #oyuncu listesi
    character_name = get_player_name("İlk", players_array)
    players_array.append(character_name)     #alınan isim oyuncu listesine ekleniyor

    character_name = get_player_name("İkinci", players_array)
    players_array.append(character_name)
    
    playing = True   #tekrar oynamak isteyen oyuncuların başlangıç noktası

    while playing:
        random.shuffle(players_array)   #oyuncu listesi karıştırılıyor.
        heads_tails = players_array[0]  #yazı tura sonucu ilk oyuncu seçiliyor.
        player = players_array[1]       #listede kalan oyuncu ikinci oyuncu olarak atanıyor.
        print("Yazı tura sonucu: {} önce başlar!".format(heads_tails))

        hp1, hp2 = (100, 100)            
        while hp1 > 1 and hp2 > 1:      #HP değerlerin 1 den büyük olması durumunda
            hp1 = attack(hp1, heads_tails)  #saldırı yapılınca hp1 değeri
            print_result(hp1, hp2, heads_tails, player)  #ve tablo oluşturma fonksiyonu çağrılır.
            if hp1 <= 1:     #hp1 oyun sırasında 0 olursa ikinci oyuncu oynamadan while döngüsü durur.
                break
            hp2 = attack(hp2, player)
            print_result(hp1, hp2, heads_tails, player)

        if hp1 <= 1:
            print("{} kazandı.".format(heads_tails))
        if hp2 <= 1:
            print("{} kazandı.".format(player))
        playing = confirm_close()         #bir oyun bittiğinde tekrar oyun oynamak için confirm_close() fonksiyonu çağrılır. 
end()