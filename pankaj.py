# importing Libraries---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import streamlit as st





#---Setting PageLayout Default to wide in this code ---------
#st.set_page_config(layout="Wide",page_title="Maissess")
st.set_page_config(page_title="Contract Details", page_icon=":memo:", layout="wide")




try:# try use  at starting of applicattion ------------------------------------------------------------

# --- Handle navigation ---------------------------------------------------------------------------------------------------------------------
  query_params = st.query_params
  page = query_params.get("page", "home")
  
  
  


  if page != "dashboard" or "Create SO" or "Approve SO":
        st.markdown("""
            <style>
            /* Navbar container */
            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: #00008B;
                padding: 10px;
            }

            /* Menu items */
            .nav-links {
                display: flex;
                gap: 15px;
            }

            .nav-links form {
                margin: 0;
            }

            .nav-links button {
                background: none;
                border: none;
                color: white;
                cursor: pointer;
                font-size: 16px;
                padding: 8px 12px;
                border-radius: 6px;
            }
            .nav-links button:hover {
                background-color: #45a049;
            }

            /* Hamburger menu (hidden on desktop) */
            .hamburger {
                display: none;
                flex-direction: column;
                cursor: pointer;
            }
            .hamburger div {
                width: 25px;
                height: 3px;
                background-color: white;
                margin: 4px;
            }

            /* Responsive behavior */
            @media (max-width: 768px) {
                .nav-links {
                    display: none;
                    flex-direction: column;
                    width: 100%;
                    background-color: #4CAF50;
                    text-align: center;
                }
                .nav-links.active {
                    display: flex;
                }
                .hamburger {
                    display: flex;
                }
            }
            </style>

            <div class="navbar">
                <div style="color:white; font-weight:bold;">MAISSESS</div>
                <div class="nav-links" id="navLinks">
                    <form method="get"><button name="page" value="home">Home</button></form>
                    <form method="get"><button name="page" value="dashboard">Dashboard</button></form>
                    <form method="get"><button name="page" value="contact">Contact</button></form>
                </div>
                <div class="hamburger" onclick="toggleMenu()">
                    <div></div>
                    <div></div>
                    <div></div>
                </div>
            </div>

            <script>
            function toggleMenu() {
                var nav = document.getElementById("navLinks");
                nav.classList.toggle("active");
            }
            </script>
        """, unsafe_allow_html=True)

    # --- Page Content ---
  if page == "home":
        st.title("🏠 Home Page")
        st.write("Welcome to the Home page!")

  elif page == "dashboard":
        st.title("📊 Dashboard Page")
        st.write("Here is your dashboard (navbar hidden).")

  elif page == "contact":
        st.title("📞 Contact Page")
        st.write("Contact us at support@example.com")






































except:# Except use at Ending of application -------------------------------------------------------------------------
  pass
















































#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

