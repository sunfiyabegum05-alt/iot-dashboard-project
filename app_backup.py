import streamlit as st
import random

st.set_page_config(
    page_title="AI Object Detection Dashboard",
    layout="wide"
)

# Sidebar
page = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Object Detection",
        "Object Mapping",
        "Detection History",
        "System Architecture",
        "Analytics",
        "Camera Feed",
        "System Status"
    ]
)

# HOME PAGE
if page == "Home":

    st.title("🤖 AI Object Detection and Mapping System")

    st.subheader("AI-Based Object Detection and Mapping Dashboard")

    st.write("### Project Information")

    st.write("Target Object : Dynamic / Unknown Object")
    st.write("Model : YOLOv8")
    st.write("Dataset Size : 401 Images")

    st.success("🟢 System Ready")

    st.write("### Project Features")

    st.write("✅ Object Detection")
    st.write("✅ Object Mapping")
    st.write("✅ YOLOv8 Based Detection")
    st.write("✅ Real-Time Monitoring Dashboard")

    st.write("### Robot Status")

    st.success("🟢 Waiting for Object")

# OBJECT DETECTION PAGE
elif page == "Object Detection":

    st.title("📷 Object Detection")

    st.image("images/controller.jpg", width=300)

    confidence = random.randint(90, 99)
    x = random.randint(200, 400)
    y = random.randint(100, 300)

    object_name = random.choice(
        ["Bottle", "Phone", "Remote", "Cup", "Mouse"]
    )

    st.metric("Objects Detected", "1")

    st.table({
        "Object": [object_name],
        "Confidence": [f"{confidence}%"],
        "X Position": [x],
        "Y Position": [y]
    })

    if confidence > 95:
        st.success(f"🟢 {object_name} Detected Successfully")
    else:
        st.warning(f"🟡 {object_name} Detected with Low Confidence")

    st.write("Detection Time: 10:35 AM")

# OBJECT MAPPING PAGE
elif page == "Object Mapping":

    st.title("🗺️ Object Mapping")

    st.info("Object Location Coordinates")

    x = random.randint(200, 400)
    y = random.randint(100, 300)

    st.table({
        "Object": ["Detected Object"],
        "X Position": [x],
        "Y Position": [y]
    })

    st.write("### Current Target Position")

    st.progress(70)

    st.success(f"Target located at X={x}, Y={y}")

    st.write("### Robot Action")

    st.info("🚗 Robot Moving Towards Target")

# DETECTION HISTORY PAGE
elif page == "Detection History":

    st.title("📋 Detection History")

    st.table({
        "Time": ["10:01", "10:05", "10:10", "10:15"],
        "Object": ["Bottle", "Phone", "Cup", "Remote"],
        "Confidence": ["98%", "97%", "99%", "96%"]
    })

# SYSTEM ARCHITECTURE PAGE
elif page == "System Architecture":

    st.title("📌 System Architecture")

    st.write("""
📷 Camera
    ↓
🤖 Object Detection Model
    ↓
🎯 Object Identification
    ↓
🗺️ Object Mapping
    ↓
📊 Streamlit Dashboard
    """)

# ANALYTICS PAGE
elif page == "Analytics":

    st.title("📊 Analytics")

    st.metric("Total Objects Detected", "25")

    st.write("Detection Summary")

    st.bar_chart([5, 8, 12, 20, 25])

# CAMERA FEED PAGE
elif page == "Camera Feed":

    st.title("🎥 Camera Feed")

    st.image(
        "images/controller.jpg",
        caption="Live Object Detection Feed (Simulation)",
        width=500
    )

# SYSTEM STATUS PAGE
elif page == "System Status":

    st.title("⚙️ System Status")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("CPU Usage", "45%")

    with col2:
        st.metric("RAM Usage", "60%")

    with col3:
        st.metric("FPS", "18")

# Footer
st.markdown("---")
st.caption("AI Object Detection Dashboard | IoT Team")