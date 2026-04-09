from flask import Flask

app = Flask(__name__)

def home():
    return '<h1>Tablet bağımlılığı; duruş bozuklukları, göz kuruluğu, obezite ve uyku düzensizliği gibi fiziksel sorunların yanı sıra, depresyon, anksiyete, dikkat eksikliği ve sosyal izolasyon gibi psikolojik ve sosyal problemlere yol açar. Özellikle çocuklarda dil gelişiminde gerileme ve akademik başarıda düşüşe neden olabilen ciddi bir dürtü kontrol bozukluğudur. --> http://127.0.0.1:5000/more <-- Tablet bağımlılığı belirtileri burada!</h1>'
@app.route("/more")
def more():
    return '<h1>Tablet Bağımlılığı Belirtileri:Zaman Kontrolünün Kaybı: "Sadece 5 dakika" diyerek saatlerce ekran başında kalmak ve süreyi yönetememek.Yoksunluk Belirtileri: Tablet ellerinden alındığında veya süre bittiğinde aşırı öfke, ağlama krizleri, huzursuzluk veya depresif ruh hali.Sosyal İzolasyon: Aile ve arkadaşlarla vakit geçirmek yerine tabletle yalnız kalmayı tercih etme.Gündelik Rutinlerin Bozulması: Yemek yemeyi reddetme, uyku saatlerinin kayması, tuvalet alışkanlıklarında düzensizlik.Hobilerin Kaybı: Eskiden keyif alınan oyun veya aktivitelerden artık zevk almama.Fiziksel Belirtiler: Uzun süre hareketsiz kalmaya bağlı boyun/sırt ağrıları, göz kuruluğu, baş ağrısı ve kilo problemleri.Yalan Söyleme/Gizleme: Tablette geçirilen süre hakkında yalan söyleme veya gizli kullanım.Duygu Düzenleme Sorunu: Can sıkıntısıyla baş edememe ve sürekli tabletle sakinleşme ihtiyacı. --> http://127.0.0.1:5000 <-- Ana Sayfa </h1>'
app.run(debug=True)