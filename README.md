# User_Story
## User Story

Projenin Amacı Kullanıcıların Sistem üzerinde kendini aktif olarak takip ederek daha verimli bir çalısşma yapmasını sağlamak

### Database
Mongodb üzerinde oluşturulan veritaban ile bağlantımızı aktif olarak kaydetmek
**todos koleksiyonu içerisinde aşağıdaki alanları içeren dökümanlar olmalıdır.**
* id (ObjectId),* 
* title (String),* 
* description (String),* 
* is_completed (Boolean), * 
* created_at (Date),  * 
* updated_at (Date) * 
### Back-End
**REST API üzerinde**
* GET methodu ile todos veriler gözükecek.*
* POST methodu ile todos koleksiyonuna veri ekleme işlemi yapılabilecek.* 
* DELETE methodu ile todos koleksiyonundan veri silme işlemi yapılabilecek. *
* PUT methodu ile todos koleksiyonunda veri güncellemesi yapılabilecek. *
### Front-End
Yapılacaklar listesi olan bir listeleme ekranı bizi karşılıcak,daha sonra
Yeni "yapılacak" maddesi eklene bilmesi için başka bir arayüz geçecez.
Listeden bir "yapılacak" maddesi  isteğe bağlı silinebilir
Tamamlanan "yapılacak" maddesi, tamamlandı olarak güncellenmektedir. 
