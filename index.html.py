<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>LABULU KABAMBA GRACIA — Portfolio</title>
  <meta name="description" content="Portfolio de Labulu Kabamba Gracia (EL-SHIMIA MOULA) — étudiant en Génie Informatique, spécialité Business Intelligence. Création d'interfaces web, gestion Instagram, débutant en IA.">
  <style>
    :root{
      --accent:#ff6f61;
      --bg:#000000;
      --card:#111;
      --muted:#9aa4b2;
      --glass: rgba(255,255,255,0.04);
      --radius:18px;
      --maxw:1100px;
      --mono: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    }
    *{box-sizing:border-box}
    body{font-family:var(--mono);margin:0;background:var(--bg);color:#e6eef6;line-height:1.5}
    .wrap{max-width:var(--maxw);margin:36px auto;padding:20px}
    header{display:flex;gap:20px;align-items:center}
    .card{background:var(--card);border-radius:20px;padding:28px;box-shadow:0 6px 24px rgba(2,6,23,0.6);}
    .hero{display:flex;flex-wrap:wrap;gap:20px}
    .hero .intro{flex:1 1 420px}
    h1{margin:0;font-size:28px}
    .title-accent{color:var(--accent)}
    .subtitle{color:var(--muted);margin-top:8px}
    .avatar{width:140px;height:140px;border-radius:16px;background:#333;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:18px;overflow:hidden}
    .avatar img{width:100%;height:100%;object-fit:cover}
    nav{display:flex;gap:10px;margin-top:14px}
    a.btn{display:inline-block;padding:8px 14px;border-radius:12px;background:var(--glass);text-decoration:none;color:inherit;font-weight:600;border:1px solid rgba(255,255,255,0.03)}
    section{margin-top:26px}
    .two-col{display:grid;grid-template-columns:1fr 340px;gap:22px}
    .skills ul{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
    .skill{background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));padding:12px;border-radius:12px;border:1px solid rgba(255,255,255,0.03)}
    .projects .project{padding:12px;border-radius:12px;background:var(--glass);margin-bottom:12px}
    footer{margin-top:36px;text-align:center;color:var(--muted);font-size:14px}
    .contact-form{display:flex;flex-direction:column;gap:10px}
    input,textarea{padding:10px;border-radius:10px;border:1px solid rgba(255,255,255,0.04);background:transparent;color:inherit}
    button.primary{background:linear-gradient(90deg,var(--accent),#ff9473);border:none;padding:10px;border-radius:12px;color:#06111a;font-weight:700}
    @media(max-width:880px){.two-col{grid-template-columns:1fr}.hero{flex-direction:column}.avatar{width:120px;height:120px}}
  </style>
</head>
<body>
  <div class="wrap">
    <header class="card hero">
      <div class="intro">
        <div style="display:flex;align-items:center;gap:14px;justify-content:space-between">
          <div>
            <h1>LABULU KABAMBA GRACIA <span class="title-accent">(EL-SHIMIA MOULA)</span></h1>
            <div class="subtitle">Étudiant en Génie Informatique — spécialité Business Intelligence — Originaire de la RDC, basé en Tunisie.</div>
          </div>
          <div class="avatar"><img src="MA_PHOTO_ICI.jpg" alt="Ma photo"></div>
        </div>
        <nav style="margin-top:16px">
          <a class="btn" href="#about">À propos</a>
          <a class="btn" href="#skills">Compétences</a>
          <a class="btn" href="#projects">Projets</a>
          <a class="btn" href="#contact">Contact</a>
        </nav>
      </div>
    </header>

    <section id="about" class="card">
      <h2>À propos de moi</h2>
      <p>Originaire de la République Démocratique du Congo et étudiant en Tunisie, je suis en Génie Informatique avec une spécialité en Business Intelligence. Curieux et motivé, j'explore chaque jour de nouvelles compétences dans le développement web, la data et l'intelligence artificielle. J'aime créer des interfaces graphiques propres, intuitives et modernes en HTML/CSS. Je gère et optimise également des comptes Instagram en combinant stratégie de contenu et méthodes techniques pour améliorer visibilité et engagement. Actuellement, je suis en formation initiale en Intelligence Artificielle pour intégrer l'IA dans mes prochains projets.</p>
    </section>

    <section class="two-col">
      <div class="card">
        <h2 id="skills">Compétences</h2>
        <div class="skills">
          <ul>
            <li class="skill">HTML / CSS — Interfaces graphiques</li>
            <li class="skill">Responsive design & UI basique</li>
            <li class="skill">JavaScript (bases)</li>
            <li class="skill">Python & Flask (notions)</li>
            <li class="skill">Business Intelligence — Analyse des données</li>
            <li class="skill">Gestion & optimisation Instagram</li>
            <li class="skill">Méthodes de boostage par présence digitale</li>
            <li class="skill">Intelligence Artificielle — Débutant</li>
          </ul>
        </div>

        <h3 style="margin-top:18px">Services</h3>
        <div style="display:flex;flex-direction:column;gap:8px">
          <div class="skill">Création d'interfaces web simples</div>
          <div class="skill">Optimisation et gestion de profils Instagram</div>
          <div class="skill">Support et formations de base en BI et IA</div>
        </div>
      </div>

      <aside class="card">
        <h3>Contact & réseaux</h3>
        <p style="color:var(--muted)">Disponible pour stages, collaborations et projets.</p>
        <p><strong>Email :</strong> <a href="mailto:gracialabulu6@gmail.com">gracialabulu6@gmail.com</a></p>
        <p><strong>WhatsApp :</strong> +21658823034</p>

        <h4 style="margin-top:12px">Link in bio</h4>
        <p style="color:var(--muted);font-size:14px">Ajoute ici le lien Linktree ou ta page bio pour regrouper tes liens.</p>
        <a class="btn" href="#contact">Me contacter</a>
      </aside>
    </section>

    <section id="projects" class="card projects">
      <h2>Projets</h2>
      <div class="project">
        <strong>Interface Portfolio (Exemple)</strong>
        <p>Une page web simple et responsive pour présenter ton profil, compétences et réalisations — idéale pour montrer ton savoir-faire en HTML/CSS.</p>
      </div>
      <div class="project">
        <strong>Gestion Instagram (Projet)</strong>
        <p>Mise en place d'une stratégie de contenu et optimisation du profil pour augmenter l'engagement et la visibilité (méthodes analytiques et automations bénignes).</p>
      </div>
      <p style="color:var(--muted)">Ajoute ici tes projets réels : captures d'écran, liens, descriptions et technologies utilisées.</p>
    </section>

    <section id="contact" class="card">
      <h2>Contact</h2>
      <p>Envie de collaborer, de booster votre présence en ligne ou de créer une interface moderne ? N'hésitez pas à me contacter — je suis ouvert aux projets, aux stages et aux opportunités.</p>

      <form class="contact-form" onsubmit="event.preventDefault(); window.location.href='mailto:gracialabulu6@gmail.com?subject=Contact%20depuis%20portfolio'">
        <input type="text" placeholder="Ton nom" required>
        <input type="email" placeholder="Ton email" required>
        <textarea rows="5" placeholder="Message"></textarea>
        <div style="display:flex;gap:8px">
          <button class="primary" type="submit">Envoyer un email</button>
          <a class="btn" href="mailto:gracialabulu6@gmail.com?subject=Demande%20de%20collaboration">Ou ouvrir mon email</a>
        </div>
      </form>
    </section>

    <footer>
      <p>© 2025 LABULU KABAMBA GRACIA — EL‑SHIMIA MOULA • Basé en Tunisie</p>
    </footer>
  </div>
</body>
</html>
