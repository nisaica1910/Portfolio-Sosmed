from flask import Flask, render_template
from markupsafe import Markup, escape

app = Flask(__name__)


@app.template_filter("bi")
def bi(t):
    """Tuple (indonesia, english) -> dua <span>, yang tampil tergantung tombol bahasa."""
    return Markup(f'<span class="id">{escape(t[0])}</span><span class="en">{escape(t[1])}</span>')


# ============ EDIT DATA DI SINI (format: ("Indonesia", "English")) ============
PROFILE = {
    "name": "Khairunnisa Ramadhan",
    "handle": "Portfolio",
    "email": "khairunnisaramadhan547@gmail.com",
    "whatsapp": "6281383094959",
    "role": ("Editor & Content Creator", "Editor & Content Creator"),
    "tagline": ("Mengolah ide menjadi konten visual yang rapi, informatif, dan mampu meningkatkan interaksi audiens.",
                "Transforming ideas into polished, informative visual content that drives audience engagement."),
    "about": ("Fresh graduate Teknik Informatika yang tertarik pada dunia kreatif, khususnya sebagai content creator dan editor. "
              "Pernah magang sebagai Content Creator selama 1 tahun di Biro Karir, Hubungan, dan Penelusuran Alumni Universitas Mercu Buana, "
              "serta berpengalaman selama 3 tahun di online shop Hatfina Hijab. "
              "Terbiasa berkomunikasi dengan baik, mengelola dan mengedit konten, serta membaca data performa untuk menentukan konten berikutnya.",
              "Fresh graduate in Informatics Engineering with a passion for creative work, especially as a content creator and editor. "
              "Completed a 1-year Content Creator internship at the Career, Relations, and Alumni Tracing Bureau of Universitas Mercu Buana, "
              "and has 3 years of experience at the online shop Hatfina Hijab. "
              "Skilled in communication, content management and editing, and reading performance data to plan what comes next."),
    "tools": ["CapCut", "Canva"],
    "socials": [
        {"name": "Instagram", "url": "https://www.instagram.com/khairu.dhan/?__pwa=1"},
        {"name": "Linkedin", "url": "https://www.linkedin.com/in/khairunnisa-ramadhan/"},
    ],
}

T = {  # teks antarmuka
    "n_about": ("Tentang", "About"), "n_work": ("Karya", "Work"), "n_ach": ("Dokumentasi", "Gallery"),
    "n_exp": ("Pengalaman", "Experience"), "n_hire": ("Hubungi aku", "Hire me"),
    "cta1": ("Lihat karya", "See my work"), "cta2": ("Lihat dokumentasi", "See the gallery"),
    "about_h": ("Tentang aku", "About me"), "tools": ("Tools", "Tools"),
    "work_h": ("Hasil konten", "Content results"),
    "work_s": ("Ini thumbnail-nya. Klik kartu untuk menonton versi lengkap di sosial media.",
               "Here are the thumbnails. Click a card to watch the full version on social media."),
    "f_all": ("Semua", "All"), "f_edit": ("Editing", "Editing"), "f_creator": ("Content Creator", "Content Creator"),
    "watch": ("Tonton", "Watch"), "views": ("views", "views"),
    "doc_h": ("Dokumentasi MC & Moderator", "MC & Moderator Gallery"),
    "doc_s": ("Beberapa momen saat aku memandu acara.", "A few moments from events I hosted."),
    "exp_h": ("Pengalaman", "Experience"), "roles_h": ("Peranku", "What I do"),
    "contact_h": ("Yuk bikin konten bareng", "Let's make content together"),
    "contact_s": ("Terbuka untuk kerja sama, magang, dan proyek freelance.",
                  "Open to collaborations, internships, and freelance projects."),
    "email_btn": ("Kirim email", "Send email"), 
    "top": ("Kembali ke atas", "Back to top"),
    "wa_btn": ("Chat WhatsApp", "Chat on WhatsApp"),
    "wa_msg": ("Halo, saya melihat portofolio kamu dan ingin berdiskusi.",
               "Hello, I saw your portfolio and would like to talk."),
    "more": ("Lihat lebih banyak", "Show more"),
    "less": ("Tampilkan lebih sedikit", "Show less"),
    "yt_h": ("Video YouTube", "YouTube Videos"),
    "yt_s": ("Versi panjang dalam format landscape. Klik untuk menonton di YouTube.",
             "Longer videos in landscape format. Click to watch on YouTube."),
}

ROLES = [
    {"title": ("Editor", "Editor"),
     "desc": ("Menyunting video dan visual sesuai konsep dan standar yang ditentukan: memilih materi, menyusun alur, sampai finalisasi supaya rapi dan mudah dipahami.",
              "Editing videos and visuals to the agreed concept and standards: picking footage, shaping the flow, and polishing the final cut so it is clean and easy to follow.")},
    {"title": ("Content Creator", "Content Creator"),
     "desc": ("Mengembangkan ide dan konsep, lalu memproduksi konten sesuai target audiens dan platform, dari perencanaan sampai eksekusi.",
              "Developing ideas and concepts, then producing content for the target audience and platform, from planning through execution.")},
    {"title": ("MC & Moderator", "MC & Moderator"),
     "desc": ("Pernah memandu acara seminar, campus hiring, dan industrial talk sebagai MC, serta menjadi moderator di talk show alumni.",
              "Hosted seminars, campus hiring, and industrial talks as an MC, and moderated an alumni talk show.")},
]

EXPERIENCES = [
    {"period": "September 2025 - September 2026", "title": ("Content Creator & Editor (Magang, 1 tahun)", "Content Creator & Editor (1-year internship)"),
     "place": "Biro Karir, Hubungan, dan Penelusuran Alumni Universitas Mercu Buana",
     "desc": ("Merancang, memproduksi, dan menyunting konten untuk sosial media resmi, mulai dari promosi seminar dan career expo, "
              "recap acara, hingga konten edukasi yang ringan dan mudah dinikmati mahasiswa maupun alumni.",
              "Planned, produced, and edited content for official social media, from seminar and career expo promos and event recaps "
              "to light educational content that students and alumni enjoy watching."),
        "ig": {"handle": "@kariralumni.umb", "url": "https://www.instagram.com/kariralumni.umb/"}},    
    {"period": "2022 - 2024", "title": ("Content Creator & Editor", "Content Creator & Editor"),
     "place": ("Hatfina Hijab (online shop)", "Hatfina Hijab (online shop)"),
     "desc": ("Membuat konten produk yang menarik dan menyuntingnya menjadi video promosi, sambil belajar bercerita singkat "
              "yang mampu menarik perhatian calon pembeli.",
              "Created eye-catching product content and edited it into promo videos, while learning short-form storytelling "
              "that captures the attention of potential buyers."),
    "ig": {"handle": "@hatfinahijab", "url": "https://www.instagram.com/hatfinahijab/"}},
]

DOCS = [  # taruh foto di static/img/, tulis nama filenya di "file"
    {"title": ("MC (Master of Ceremony)", "MC (Master of Ceremony)"),
     "desc": ("Seminar pelatihan, campus hiring, dan industrial talk.", "Training seminars, campus hiring, and industrial talks."),
     "c": "c1",
     "photos": [
         {"file": "mc1.jpg", "cap": ("Seminar pelatihan", "Training seminar")},
         {"file": "mc3.jpg", "cap": ("Industrial talk", "Industrial talk")}, 
         {"file": "mc2.jpg", "cap": ("Campus hiring", "Campus hiring"), "wide": True}, 
     ]},
    {"title": ("Moderator", "Moderator"),
     "desc": ("Memandu diskusi di acara talk show alumni.", "Moderating discussions at an alumni talk show."),
     "c": "c2",
     "photos": [
         {"file": "mod1.png", "cap": ("Alumni Talks (live)", "Alumni Talks (live)")},
         {"file": "mod2.jpeg", "cap": ("Bersama narasumber", "With the guest speaker")},
     ]},
]

# cat: "edit" atau "creator". Thumbnail: taruh di static/img/, tulis nama file di "thumb".
# Judul di bawah ini contoh dari kerjaan serupa; ganti dengan karyamu. Kalau file gambar belum ada, tampil gradient.
_RAW = [
    # --- Tracer Study ---
    ("Tracer Study 2026 (Versi Indonesia)", "Tracer Study 2026 (Indonesian Version)",
     "https://www.instagram.com/kariralumni.umb/reel/DbKJGlip2tX/", "tracer-2026-id.jpg"),
    ("Tracer Study 2026 (English Version)", "Tracer Study 2026 (English Version)",
     "https://www.instagram.com/kariralumni.umb/reel/DcNft33p-SC/", "tracer-2026-en.jpg"),
    ("Info Tracer Study (English Version)", "Tracer Study Info (English Version)",
     "https://www.instagram.com/reel/DXqHLeOiT3j/", "tracer-info-en.jpg"),
    ("Promosi Tracer Games", "Tracer Games Promo",
     "https://www.instagram.com/reel/Dag5KIiJZRa/", "tracer-games.jpg"),
    ("Promosi Tracer Study & Tracer Games", "Tracer Study & Tracer Games Promo",
     "https://www.instagram.com/kariralumni.umb/reel/DawYyAtJhNl/", "tracer-promo.jpg"),

    # --- Wisuda ---
    ("Wawancara Wisudawan Batch 1 2026", "Graduate Interviews, Batch 1 2026",
     "https://www.instagram.com/reel/DYYjnqrprVA/", "wisuda-wawancara.jpg"),
    ("Tanya-Tanya Orang Tua Wisudawan", "Asking the Graduates' Parents",
     "https://www.instagram.com/kariralumni.umb/reel/DYYq-4pp01x/", "wisuda-ortu.jpg"),
    ("Wisuda Core", "Graduation Core Team",
     "https://www.instagram.com/kariralumni.umb/reel/DYeBh8Spq_U/", "wisuda-core.jpg"),
    ("Tanya-Tanya Wisudawan UMB", "Asking UMB Graduates",
     "https://www.instagram.com/reel/DS30mddCYMX/", "wisuda-tanya1.png"),
    ("Tanya-Tanya Wisudawan UMB (Part 2)", "Asking UMB Graduates (Part 2)",
     "https://www.instagram.com/reel/DS32xGNiYBN/", "wisuda-tanya2.jpg"),

    # --- Konten Fun ---
    ("Konten Fun: 5 Rekomendasi Makanan di Kampus", "Fun Content: 5 Food Recommendations on Campus",
     "https://www.instagram.com/reel/DW5LezdCZb9/", "fun-makanan.jpg"),
    ("Tipe-Tipe Karyawan Saat Puasa", "Types of Employees While Fasting",
     "https://www.instagram.com/reel/DVITe4qiTum/", "fun-puasa.png"),
    ("Ayo Gowes ke Kampus", "Let's Cycle to Campus",
     "https://www.instagram.com/kariralumni.umb/reel/DbC06EcJTS3/", "fun-gowes.jpg"),
    ("Merdeka Versi Kamu Apa?", "What Does Independence Mean to You?",
     "https://www.instagram.com/kariralumni.umb/reel/DcK7sHqpVin/", "fun-merdeka.jpg"),
    ("Ucapan Hari Kemerdekaan", "Independence Day Greeting",
     "https://www.instagram.com/kariralumni.umb/reel/DcIi-Wnp5hG/", "fun-ucapan-merdeka.jpg"),
    ("Info Lokasi Parkiran UMB", "UMB Parking Location Info",
     "https://www.instagram.com/reel/DXD6y8mieE7/", "info-parkiran.jpg"),

    # --- Promosi & Info ---
    ("Teaser Seminar & Workshop Series", "Seminar & Workshop Series Teaser",
     "https://www.instagram.com/reel/DWnlq-0CY9g/", "promo-teaser.jpg"),
    ("Promosi Seminar di Mercu Buana", "Seminar Promo at Mercu Buana",
     "https://www.instagram.com/kariralumni.umb/reel/DW0FT3fCWZM/", "promo-seminar1.jpg"),
    ("Promosi Seminar", "Seminar Promo",
     "https://www.instagram.com/kariralumni.umb/reel/DZOwqEVJ2CI/", "promo-seminar2.jpg"),
    ("Do's & Don'ts Career Expo 2025 UMB", "Career Expo 2025 UMB Do's & Don'ts",
     "https://www.instagram.com/reel/DPA7VSCiRf8/", "expo-dos-donts.png"),
    ("Tanya-Tanya Perusahaan Career Expo", "Asking Companies at the Career Expo",
     "https://www.instagram.com/reel/DPVlp89icLS/", "expo-tanya.jpg"),
    ("Tips Networking", "Networking Tips",
     "https://www.instagram.com/kariralumni.umb/reel/DXvt6ukpqbY/", "tips-networking.jpg"),
    ("Informasi MagangHub", "MagangHub Information",
     "https://www.instagram.com/kariralumni.umb/reel/DZY4BKIJUTQ/", "info-maganghub.jpg"),
    ("Test Ride Produk Motor PT Rindang Kurnia Motor", "Motorcycle Test Ride, PT Rindang Kurnia Motor",
     "https://www.instagram.com/reel/DZ_6x-DJCUD/", "testride.jpg"),
    ("Promosi Workshop Simulasi Wawancara", "Interview Simulation Workshop Promo",
     "https://www.instagram.com/kariralumni.umb/reel/Daty8CzprUv/", "promo-simulasi-wawancara.jpg"),
    ("UMB Goes to Singapore", "UMB Goes to Singapore",
     "https://www.instagram.com/kariralumni.umb/reel/DcaKPPrp4xO/", "singapore.png"),

    # --- Recap (paling bawah) ---
    ("Recap Career Readiness & Future Skills UMB", "Career Readiness & Future Skills Recap, UMB",
     "https://www.instagram.com/reel/DQlckg2CTIJ/", "recap-career-readiness.jpg"),
    ("Rekap Industrial Talk bersama PT Usaha Sukses (Tyeso Indonesia)", "Industrial Talk Recap with PT Usaha Sukses (Tyeso Indonesia)",
     "https://www.instagram.com/reel/DRQp4hOk1nH/", "recap-tyeso.jpg"),
    ("Rekap Industrial Talk bersama Gojek Tokopedia", "Industrial Talk Recap with Gojek Tokopedia",
     "https://www.instagram.com/reel/DX0aUrlpoqp/", "recap-gojek.jpg"),
    ("Rekap Open House Universitas Mercu Buana 2025", "Universitas Mercu Buana Open House 2025 Recap",
     "https://www.instagram.com/reel/DRvl2pfE8kR/", "recap-openhouse.jpg"),
    ("Recap Wisuda UMB 2025", "UMB Graduation 2025 Recap",
     "https://www.instagram.com/reel/DSoqvqfCTAQ/", "recap-wisuda-2025.jpg"),
    ("Rekap Wisuda Batch 1 2026", "Graduation Batch 1 2026 Recap",
     "https://www.instagram.com/reel/DYYZIGCpCsp/", "recap-wisuda-2026.jpg"),
]

CONTENTS = [{"title": (t[0], t[1]), "url": t[2], "thumb": t[3], "c": f"c{i % 6 + 1}"}
            for i, t in enumerate(_RAW)]

YOUTUBE = [  # "id" = kode setelah v= di link YouTube
    {"id": "J2JBFbqfzrU",
     "title": ("Promosi Tracer Study untuk Kebutuhan Wisuda Universitas Mercu Buana 2025",
               "Tracer Study Promo for the Universitas Mercu Buana 2025 Graduation"),
     "tools": "CapCut",
     "thumb": "yt1.jpg"},
]
# ==============================================================================


@app.route("/")
def index():
    return render_template("index.html", p=PROFILE, t=T, docs=DOCS,
                           roles=ROLES, exps=EXPERIENCES, contents=CONTENTS, youtube=YOUTUBE)


if __name__ == "__main__":
    app.run(debug=True, port=5005)
