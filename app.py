import streamlit as st
from supabase import create_client
from datetime import datetime, timezone

# Supabase vorbereiten

supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

# Bekommen der Information

st.text("Gebe deine Information ein")
information = st.text_input("Information")
wichtig_aktiv = st.toggle("Ist die Information wichtig?")

# Speichern der Information

if st.button("Speichern"):
    now_iso = datetime.now(timezone.utc).isoformat()
    supabase.table("infortmationen").insert({   
        "Informationen": information,    
        "Wichtig": bool(wichtig_aktiv),
        "Datum": now_iso,  # ✅ JSON serializable
    }).execute()
    st.success("Speichern erfolgreich")

# Zeigen der Information

st.text("Infos")
result = supabase.table("infortmationen").select("*").limit(50).execute()

st.write(result.data)
