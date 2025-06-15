import streamlit as st


def home():
    st.markdown(
        """
        <div style='text-align: center'>
            <h1>Dorian Ratzmer</h1>
            <h3>IHK - zertifizierter Datenanalyst - Power BI, Python, SQL</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.image(r"C:\Users\Admin\Desktop\DataCraft\Bewerbungsphase\images\Dorian_Nordsee.jpg", width=250)

def about_me():
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Was mich ausmacht</h2>
            Aus meiner langjährigen Tätigkeit in der persönlichen Assistenz bringe ich ein hohes Maß an Verantwortungsbewusstsein, Kommunikationsstärke und Organisationstalent mit.<br>
            In meiner aktuellen Weiterbildung zum Data Analyst habe ich gelernt, diese Fähigkeiten mit analytischem Denken und technischem Know-how zu verbinden.<br>
            Ich arbeite selbstständig, lerne schnell neue Tools und Methoden kennen und bin motiviert, meine Kenntnisse kontinuierlich auszubauen und im Team einzubringen.
            Besonders wichtig sind mir dabei eine strukturierte Arbeitsweise und Zuverlässigkeit – Eigenschaften, die ich über viele Jahre in anspruchsvollen, verantwortungsvollen Tätigkeiten verfeinert habe.
            Meine Erfahrung im Umgang mit Menschen mit besonderen Bedürfnissen hat meine soziale Kompetenz und Empathie gestärkt, die ich heute auch in datengetriebenen Projekten nutze, um komplexe Sachverhalte verständlich aufzubereiten.
            Zudem bin ich es gewohnt, in stressigen Situationen den Überblick zu behalten und Lösungen zielorientiert umzusetzen.
            Ich suche eine Position, in der ich meine Fähigkeiten als kommunikativer und analytischer Teamplayer weiterentwickeln kann – idealerweise in einem Umfeld, das Innovation fördert und persönliche Weiterentwicklung unterstützt.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Mein Skillset</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    skills = ["Power BI", "SQL", "Excel", "Python", "Projektmanagementtools", "Teamfähigkeit"]

    # 2 Reihen mit je 3 Skills
    cols1 = st.columns(3)
    for i, skill in enumerate(skills[:3]):
        with cols1[i]:
            st.markdown(f"<div style='text-align: center; font-weight: bold;'>{skill}</div>", unsafe_allow_html=True)
    cols2 = st.columns(3)
    for i, skill in enumerate(skills[3:]):
        with cols2[i]:
            st.markdown(f"<div style='text-align: center; font-weight: bold;'>{skill}</div>", unsafe_allow_html=True)

    st.markdown("---")


def skills():
    st.title("Berufliche Erfahrung & Kenntnisse")

    st.header("Berufserfahrung")

    st.markdown("### Persönlicher Assistent von Menschen mit Behinderung")
    st.markdown("*FAB eV Kassel, 2010-2023*")
    st.markdown(
        """
        In dieser Tätigkeit habe ich umfassende Erfahrung im eigenverantwortlichen Arbeiten und im Umgang mit sensiblen Situationen gesammelt.  
        Besonders wichtig waren dabei Kommunikationsstärke, Empathie und die Fähigkeit, individuelle Bedürfnisse zuverlässig zu unterstützen.  
        Außerdem habe ich ein Team von Assistent:innen koordiniert und organisatorische Abläufe effizient gestaltet.
        """
    )
    st.markdown("---")

    st.markdown("### Helfer in der Pflege")
    st.markdown("*GDA Wohnstift Göttingen, 2007-2010*")
    st.markdown(
        """
        Die Arbeit in der Pflege hat mir einen tiefen Einblick in strukturierte Arbeitsprozesse und interdisziplinäre Zusammenarbeit vermittelt.  
        Hier habe ich insbesondere meine Belastbarkeit, Ausdauer und Sorgfalt im täglichen Umgang mit Menschen und medizinischen Anforderungen gestärkt.  
        Zudem konnte ich wertvolle Erfahrungen im Bereich Dokumentation und Qualitätsmanagement sammeln.
        """
    )
    st.markdown("---")

    st.markdown("### Diverse (Neben)Jobs")
    st.markdown("*In 13/16 Bundesländern Deutschlands, 2004-2010*")
    st.markdown(
        """
        In dieser Zeit habe ich mir durch vielfältige Tätigkeiten – u.a. im Handwerk, in sozialen Projekten, in der Gastronomie und im kreativen Bereich –  
        eine ausgeprägte Anpassungsfähigkeit und hohe Lernbereitschaft angeeignet. Die ständige Einarbeitung in neue Aufgaben und Teams hat meine Flexibilität,  
        mein Improvisationstalent und meine Neugier auf neue Themen entscheidend gefördert. Gleichzeitig habe ich gelernt,  
        mich in sehr unterschiedlichen sozialen und kulturellen Umfeldern sicher zu bewegen.
        """
    )

    st.markdown("---")

    st.header("Kenntnisse und Fähigkeiten")
    skills_list = [
        "Organisation und Koordination von Arbeitsabläufen",
        "Kommunikationsfähigkeit",
        "Empathie und soziale Kompetenz",
        "Verantwortungsbewusstsein",
        "Belastbarkeit und Stressresistenz",
        "Teamführung und Zusammenarbeit",
        "Flexibilität und schnelle Einarbeitung in neue Aufgaben",
        "Interkulturelle Kompetenz",
        "Selbstständige und strukturierte Arbeitsweise"
    ]

    for skill in skills_list:
        st.markdown(f"- {skill}")

    st.markdown("---")

    st.header("Ausbildung")
    st.markdown("**Realschule West Gießen, 2001** – Realschulabschluss  ")
    st.markdown("**Geb. Nikolaus GmbH Gießen, 2001-2004** – Maler und Lackierer")

    st.header("Sprachen")
    st.markdown("- Deutsch (Muttersprache)")
    st.markdown("- Englisch (B2)")


def projects():
    st.title("Projekte")
    st.write(
        "**Hier präsentiere ich ein paar meiner Projekte, welche wir in unseren Projekttagen, am Ende der jeweiligen Umschulungsmodule, in Teamarbeit umgesetzt haben."
        "Weitere befinden sich auf GitHub (Link unter 'Kontakt')**")

    st.subheader("FunFacts")
    st.markdown(
        "In diesem Projekt wurden über eine API-Abfrage 365 FunFacts in einer Datenbank gespeichert, "
        "um sich diese mit einer App wiedergeben lassen zu können. Einzelne Fakten können als Favoriten gespeichert werden und eine kleine Statistik gibt es auch."
    )
    st.image(r"C:\Users\Admin\Desktop\DataCraft\Bewerbungsphase\images\Schreenshot_Fun_Fact_Generaator.png")

    st.markdown("---")
    st.write("")
    st.markdown(
        "Hier eines der früheren Projekte, bei dem es darum ging, Daten zu visualisieren. Wir haben dazu Wetterdaten aus dem Internet extrahiert, "
        "um sie via Streamlit sichtbar zu machen."
    )

    # Nebeneinander mit st.columns und kleinere Bilder (z.B. Breite 300 px)
    col1, col2 = st.columns(2)
    with col1:
        st.image(r"C:\Users\Admin\Desktop\DataCraft\Bewerbungsphase\images\Screenshot_Wetterapp2.png", width=300)
    with col2:
        st.image(r"C:\Users\Admin\Desktop\DataCraft\Bewerbungsphase\images\Screenshot_Wetterapp3.png", width=300)

    st.markdown("---")
    st.markdown(
        "Das Dashboard, mit dem mein Team und ich bei der IHK-Prüfung überzeugt haben, darf hier natürlich auch auf keinen Fall fehlen. "
        "Hier ging es darum, anhand von Daten eines Fitnessstudios zu errechnen, welche Kunden ihre Verträge nicht verlängern werden "
        "und für die Marketingabteilung entsprechende Kundenprofile herauszuarbeiten."
    )
    st.image(r"C:\Users\Admin\Desktop\DataCraft\Bewerbungsphase\images\IHK_Dashboard.png")


def contact():
    st.title("Kontakt")

    st.header("Persönliche Kontaktdaten")
    st.write("📧 Email: ratzmer.d86@gmail.com")
    st.write("📞 Telefon: 0163/2441358")
    st.write("🏠 Adresse: 34117 Kassel, Deutschland")

    st.markdown("---")

    st.header("Social Media")
    st.write("LinkedIn: https://www.linkedin.com/in/dorian-r-382692344/")
    st.write("")
    st.write("GitHub: [github.com/dorianratzmer](https://github.com/Ameroras)")

    st.markdown("---")

    st.write("© 2025 Dorian Ratzmer")



st.set_page_config(page_title="Lebenslauf Dorain Ratzmer")
st.sidebar.title("Übersicht")
page = st.sidebar.radio("Gehe zu", ["Startseite","Was mich ausmacht", "Fähigkeiten", "Projekte", "Kontakt"])

if page == "Startseite":
    home()
elif page == "Was mich ausmacht":
    about_me()
elif page == "Fähigkeiten":
    skills()
elif page == "Projekte":
    projects()
elif page == "Kontakt":
    contact()
