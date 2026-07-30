<!DOCTYPE html>
<html lang="tr">

<head>
    <meta charset="UTF-8">
    <title>Elvin Ahlatcı</title>

    <!-- Yazı fontu -->
    <link href="https://fonts.googleapis.com/css?family=Saira+Extra+Condensed:700"
          rel="stylesheet">

    <!-- GitHub simgesi -->
    <script src="https://use.fontawesome.com/releases/v5.13.0/js/all.js"></script>

    <style>

        body {
            margin: 0;
            font-family: Arial;
            background-color: #fafafa;
        }

        /* Sol siyah alan */
        nav {
            width: 270px;
            height: 100vh;
            background-color: black;
            position: fixed;

            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Profil fotoğrafı */
        img {
            width: 180px;
            height: 180px;

            object-fit: cover;
            border-radius: 50%;

            border: 8px solid #555;
            transform: translateY(-70px);
        }

        /* Sağ taraf */
        main {
            margin-left: 250px;
            padding: 170px 70px;
        }

        /* İsim */
        h1 {
            font-family: "Saira Extra Condensed";
            font-size: 100px;

            margin: 0;
            line-height: 1;
        }

        /* Soyadın rengi */
        .soyad {
            color: #777;
        }

        /* İsmin altındaki yazı */
        h2 {
            font-family: "Saira Extra Condensed";
            font-size: 30px;

            color: #666;

            margin-top: 0;
            margin-bottom: 20px;
        }

        /* Açıklama */
        p {
            font-size: 20px;
            color: #555;
        }

        /* GitHub simgesi */
        .github {
            width: 60px;
            height: 60px;

            background-color: #334;
            color: white;

            border-radius: 50%;

            display: flex;
            justify-content: center;
            align-items: center;

            font-size: 30px;

            text-decoration: none;
            margin-top: 25px;
        }

    </style>

</head>

<body>

    <nav>
        <img src="WhatsApp Image 2026-07-28 at 16.51.44.jpeg" alt="Profil fotoğrafı">
    </nav>

    <main>

        <h1>
            ELVİN <span class="soyad">AHLATCI</span>
        </h1>

        <h2>
     YONETIM BILISIM SISTEMLERI ADAYI
      </h2>
    
       <p>
    Yazılım, bilişim sistemleri ve dijital teknolojiler alanında
    kendimi geliştirerek gelecekte yenilikçi projeler üretmeyi hedefliyorum.
      </p>
        </p>

        <a class="github"
           href="https://github.com/ElvinAhlatci"
           target="_blank">

            <i class="fab fa-github"></i>

        </a>

    </main>

</body>

</html>
