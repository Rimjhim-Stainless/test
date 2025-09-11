import streamlit as st

# -------------------
# Inject Custom CSS
# -------------------





  # defining session state ---------------------------------------------------------------------------------------------------------------
import streamlit as st
if "show_form" not in st.session_state:
                st.session_state.show_form = False












#showing main page after login 


if not st.session_state.show_form:
        #css for tppbar    

        st.markdown("""    
            <style>
            .topbar {
                width: 100%;
                background-color: #0b2343 !important;  /* force dark blue */
                color: white;
                font-size: 16px;
                padding: 12px 20px;
                text-align: center;
            }
            </style>

            <div class="topbar">
                ✅ This is the DARK BLUE STRIP (Topbar)
            </div>
        """, unsafe_allow_html=True)

       

        st.markdown("""
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

            <style>
            /* Reset Streamlit background and padding */
            html, body, [class*="stApp"] {
                background-color: #ffffff !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            .block-container {
                padding: 0 !important;
                margin: 0 !important;
                max-width: 100% !important;
            }

            /* ✅ Topbar */
            .topbar {
                width: 100%;
                background-color: #0b2343;  /* dark navy */
                color: white;
                font-size: 14px;
                padding: 6px 20px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                flex-wrap: wrap;
                box-sizing: border-box;
            }
            .topbar .left span {
                margin-right: 15px;
                color: #ffcc00;
            }
            .topbar .right {
                display: flex;
                align-items: center;
                flex-wrap: wrap;
            }
            .topbar .right span {
                margin-left: 15px;
                color: white;
            }

            /* ✅ Social Media Buttons */
            .social-icons a {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                width: 32px;
                height: 32px;
                margin-left: 8px;
                border-radius: 50%;
                background-color: transparent;
                border: 1px solid #ffcc00;
                color: #ffcc00;
                text-decoration: none;
                font-size: 14px;
                transition: all 0.3s ease;
            }
            .social-icons a:hover {
                background-color: #ffcc00;
                color: #0b2343;
            }

            /* ✅ Navbar */
            .navbar {
                width: 100%;
                background-color: white;
                padding: 10px 20px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 1px solid #eee;
                flex-wrap: wrap;
                box-sizing: border-box;
            }
            .navbar .logo {
                font-size: 22px;
                font-weight: 700;
                color: #0b2343;
                display: flex;
                align-items: center;
            }
            .navbar .logo i {
                margin-right: 6px;
                color: #0b2343;
            }
            .navbar .menu {
                display: flex;
                align-items: center;
                flex-wrap: wrap;
            }
            .navbar .menu a {
                margin: 0 12px;
                font-weight: 600;
                color: #0b2343;
                text-decoration: none;
            }
            .navbar .menu a.active {
                color: #ffcc00;
            }
            .navbar .menu a:hover {
                color: #ffcc00;
            }
            .navbar .button {
                background-color: #ffcc00;
                color: #0b2343;
                font-weight: 600;
                padding: 8px 18px;
                border-radius: 4px;
                text-decoration: none;
                margin-left: 20px;
            }
            .navbar .button:hover {
                background-color: #e6b800;
            }

            /* ✅ Responsive */
            @media (max-width: 768px) {
                .navbar {
                    flex-direction: column;
                    align-items: flex-start;
                }
                .navbar .menu {
                    flex-direction: column;
                    width: 100%;
                    margin-top: 10px;
                }
                .navbar .menu a {
                    margin: 8px 0;
                }
                .navbar .button {
                    margin-top: 12px;
                    margin-left: 0;
                    align-self: flex-start;
                }
            }
            </style>
        """, unsafe_allow_html=True)


# css for button and defining buttom 




        st.markdown("""
        <style>
        .button-primary {
            background-color: #3B5998;
            color: white;
            padding: 10px 25px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            font-weight: bold;
            margin-right: 10px;
        }
        .button-accent {
            background-color: #FF4081;
            color: white;
            padding: 10px 25px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            font-weight: bold;
            margin-right: 10px;
        }
        .button-warn {
            background-color: #F44336;
            color: white;
            padding: 10px 25px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True)

        # -------------------
        # ✅ HTML Structure
        # -------------------
        st.markdown("""
            <!-- Topbar -->
            <div class="topbar">
                <div class="left">
                    <span><i class="fas fa-map-marker-alt"></i> /////</span>
                    <span><i class="far fa-clock"></i> /////</span>
                </div>
                <div class="right">
                    <span><i class="fas fa-phone-alt"></i> +91 0000000</span>
                    <div class="social-icons">
                        <a href="#"><i class="fab fa-facebook-f"></i></a>
                        <a href="#"><i class="fab fa-twitter"></i></a>
                        <a href="#"><i class="fab fa-linkedin-in"></i></a>
                        <a href="#"><i class="fab fa-instagram"></i></a>
                    </div>
                </div>
            </div>

            
            
            </div>
        """, unsafe_allow_html=True)

        # -------------------
        # Example Content
        import streamlit as st

        # Load FontAwesome
        #st.markdown("""
        # <link rel="stylesheet" 
                #  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
        #""", unsafe_allow_html=True)

        # Create navbar row
        col1, col2 ,col3,col4,col5,col6= st.columns([1.5,3,1,1,1,1])

        with col1:
            st.markdown('<div style="font-size:22px; font-weight:bold; color:#0b2343;">'
                        '<i class="fas fa-graduation-cap"></i> MAISSSESS</div>', 
                        unsafe_allow_html=True)
            st.markdown(
            '<div style="font-size:10px; font-weight:bold; color:#0FFF50"> (Your GateWay to Seamless Online Order) </div>',
            unsafe_allow_html=True
        )

            

        with col2:
            st.markdown('<div style="font-size:25px; font-weight:bold; color:#00008B;">'
                        ' Welcome to Rimjhim Ispat  Order  Portal</div>', 
                        unsafe_allow_html=True)
            
        with col3:
                st.markdown('<div style="margin-top: 1px;"></div>', unsafe_allow_html=True)
                if st.button("Create SO", key="hhe"):
                        st.session_state.show_form=True
                        st.rerun()

                # Add inline style for button look
                st.markdown("""
                    <style>
                        div.stButton > button:first-child {
                            background-color: #00008B;
                            color: white;
                            padding: 10px 25px;
                            border-radius: 0px;
                            border: none;
                            font-weight: bold;
                        }
                    </style>
                """, unsafe_allow_html=True)

        with col4:
                st.markdown('<div style="margin-top: 1px;"></div>', unsafe_allow_html=True)
                if st.button("Approve SO", key="jeie"):
                        st.write("")
                        

                # Add inline style for button look
                st.markdown("""
                    <style>
                        div.stButton > button:first-child {
                            background-color: #00008B;
                            color: white;
                            padding: 10px 25px;
                            border-radius: 0px;
                            border: none;
                            font-weight: bold;
                        }
                    </style>
                """, unsafe_allow_html=True)
        with col5:
                st.markdown('<div style="margin-top: 1px;"></div>', unsafe_allow_html=True)
                if st.button("Dashboard", key="nn"):
                        st.write("")
                # Add inline style for button look
                st.markdown("""
                    <style>
                        div.stButton > button:first-child {
                            background-color: #00008B;
                            color: white;
                            padding: 10px 25px;
                            border-radius: 0px;
                            border: none;
                            font-weight: bold;
                        }
                    </style>
                """, unsafe_allow_html=True)



        import streamlit as st
        from PIL import Image, ImageDraw, ImageFont

        import streamlit as st
        from PIL import Image, ImageDraw, ImageFont

        # Load your image
        image_path = "images.jpeg"  # Replace with your image path
        import streamlit as st
        from PIL import Image, ImageDraw, ImageFont

        # Load your image
        # Replace with your image path
        image = Image.open(image_path)

        # Resize the image (e.g., width=600 while maintaining aspect ratio)


        # Load your image
        #image_path = "your_image_path.jpg"  # Replace with your image path
        image = Image.open(image_path)

        # Resize the image (e.g., width=600 while maintaining aspect ratio)
        base_width = 400
        w_percent = (base_width / float(image.size[0]))
        h_size = int((float(image.size[1]) * float(w_percent)))
        image = image.resize((base_width, h_size), Image.Resampling.LANCZOS)

        # Add text on image
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 40)  # Adjust font and size
        text = "Rimjhim Ispat Ltd"

        # Center the text
        width, height = image.size
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        position = ((width - text_width) / 1.5, 80)  # 20 pixels from top

        draw.text(position, text, font=font, fill="white")

        # Display in Streamlit


        st.image(image,width=1600)

        # Optional: Styled heading below image
        st.markdown(
            '<div style="font-size:22px; font-weight:bold; color:#0b2343">Your GateWay to Seamless Online Order</div>',
            unsafe_allow_html=True
        )
















# Sales Order Creation form Code Start from Here ----------------------------------------------------------------------------------------------------------------------------------




if st.session_state.show_form:


        st.title("Sales Order Creation Form")
    
    
        
        st.write("Fill Form that is given below,* Marked Field are compulsary to enter ")
        col10,col12,col13,col14,col15,col16,col17=st.columns(7)
        with col10:
                Party_So=st.text_input("Party Name * ")

        with col12:
                Contract_Number=st.text_input("Contract Number*")
        with col13:
                Grade=st.text_input("Grade")
        with col14:
                Material_Description=st.text_input("Material Description")
        with col15:
                Rate=st.text_input("Rate")
        with col16:
                Sauda_Pending_Qty=st.text_input("Pending Qty ")
        with col17:
                Ship_to=st.text_input("Ship to ")
                
        






# Close Button to Close Sales Order Creation Window

        close=st.button('cLOSE')
        if close:
                st.session_state.show_form=False
                st.rerun()


















































# Footer Code start from Here --------------------------------------------------------------------------------------------------------------------------------------------------


import streamlit as st
if not st.session_state.show_form:
            import streamlit as st

# Footer styling container
            st.markdown("""
            <div style="width:100%; background-color:#0b2343; color:white; padding:40px 20px; box-sizing:border-box;">
                <div style="max-width:1200px; margin:auto; display:flex; flex-wrap:wrap; gap:30px;">
                    <div style="flex:1 1 250px;">
                        <h4 style="color:white; margin-bottom:15px;">Get In Touch</h4>
                        <h3 style="color:#FFD700; margin-bottom:15px;">📌 RIMJHIM ISPAT LIMITED</h3>
                        <p>📍 AKARAMPUR, UNNAO (U.P)</p>
                        <p>📞 +91 0000000</p>
                        <p>✉️ @gmail.com</p>
                    </div>
                    <div style="flex:1 1 150px;">
                        <h4 style="color:white; margin-bottom:15px;">Quick Links</h4>
                        <a href="#" style="display:block; color:white; text-decoration:none; margin-bottom:5px;">Book Contract</a>
                        <a href="#" style="display:block; color:white; text-decoration:none; margin-bottom:5px;">Create SO</a>
                        <a href="#" style="display:block; color:white; text-decoration:none;">Logout</a>
                    </div>
                    <div style="flex:1 1 250px;">
                        <h4 style="color:white; margin-bottom:10px;">Newsletter</h4>
            """, unsafe_allow_html=True)

            # Streamlit interactive elements


            st.markdown("""
                        <h6 style="color:white; margin-bottom:10px;">Follow Us</h6>
                        <div style="display:flex; gap:5px;">
                            <a href="#" style="color:white; border:1px solid white; padding:8px; border-radius:50%;"><i class="fab fa-twitter"></i></a>
                            <a href="#" style="color:white; border:1px solid white; padding:8px; border-radius:50%;"><i class="fab fa-facebook-f"></i></a>
                            <a href="#" style="color:white; border:1px solid white; padding:8px; border-radius:50%;"><i class="fab fa-youtube"></i></a>
                            <a href="#" style="color:white; border:1px solid white; padding:8px; border-radius:50%;"><i class="fab fa-linkedin-in"></i></a>
                        </div>
                    </div>
                </div>
            </div>

            <div style="width:100%; background-color:#0a1f3f; color:white; padding:15px 20px; text-align:center;">
                &copy; <a href="#" style="color:#FFD700; text-decoration:none;">RIMJHIM ISPAT LIMITED</a>, All Rights Reserved. 
                Designed By <a href="#" style="color:#FFD700; text-decoration:none;">Rimjhim Team</a>
            </div>
            """, unsafe_allow_html=True)


            # Load Font Awesome for icons

