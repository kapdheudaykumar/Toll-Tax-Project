import streamlit as st
import pandas as pd
if "vehicles" not in st.session_state:
    st.session_state.vehicles = []
st.title("Toll Tax Management System")
st.subheader("Enter Vehicle Details")
vehicle_number = st.text_input("Enter Vehicle Number")
owner_name = st.text_input("Enter Owner Name")
vehicle_type = st.selectbox("Select Vehicle Type",["Bike", "Car", "Truck"])
if vehicle_type == "Bike":
    tax = 20
elif vehicle_type == "Car":
    tax = 50
else:
    tax = 100
if st.button("Add Vehicle"):
    vehicle = {"Vehicle Number": vehicle_number,"Owner Name": owner_name,"Vehicle Type": vehicle_type,"Toll Tax": tax}
    st.session_state.vehicles.append(vehicle)
    st.success("✅ Vehicle Added Successfully!")
if len(st.session_state.vehicles) > 0:
    st.subheader("Vehicle Records")
    df = pd.DataFrame(st.session_state.vehicles)
    st.dataframe(df)
    total = 0
    for v in st.session_state.vehicles:
        total += v["Toll Tax"]
    st.subheader("Total Toll Collection")
    st.success(f"₹ {total}")
else:
    st.info("No Vehicle Records Available")