import streamlit as st
import datetime
import os
from PIL import Image
from astropy.time import Time

# path = os.getcwd()
# path = 'D:/SolO_epd_py/Summary_plot/summary_plot_page'
# path = 'https://github.com/EpsilonLwy/streamlit_summary_plot/master'
path = './Plot'
# st.markdown("# Summary Plot Overview")
st.title('Summary Plot Overview')
select_day = st.sidebar.date_input("Select Date", datetime.date(2022, 1, 1))
name = str(select_day.year) + str(select_day.month).rjust(2, '0') + str(select_day.day).rjust(2, '0')
start_time = Time(str(select_day), format='isot', scale='utc')
# end_time = Time(start_time.jd+1, format='jd', scale='utc')
# st.markdown('## Time Range：'+start_time.isot[0:10].replace('-', '/')+' — '+end_time.isot[0:10].replace('-', '/'))
st.markdown('## Time Range：' + start_time.isot[0:10].replace('-', '/'))
# st.markdown('## Time Range：' + str(select_day).replace('-', '/'))

st.header('1. Solar Orbiter')
col1, col2 = st.columns(2)
with col1:
    st.header("(1) STEP-EPT (res:3min)")
    file_step_ept = path.replace('\\', '/') + '/Summary_Plot/Solar-Orbit/EPD/step-ept/' + str(select_day.year) + '/step_ept_electron_ion_' + name + '.png'
    print(file_step_ept)
    if os.path.isfile(file_step_ept):
        st.image(Image.open(file_step_ept))
        print('yes')
    else:
        st.write('N/A')
with col2:
    st.header("(2) SWA-MAG (res:3min)")
    file_swa_mag = path.replace('\\', '/') + '/Summary_Plot/Solar-Orbit/SWA-MAG/' + str(select_day.year) + '/pas_mag_' + name + '.png'
    if os.path.isfile(file_swa_mag):
        st.image(Image.open(file_swa_mag))
    else:
        st.write('N/A')
col1, col2 = st.columns(2)
with col1:
    st.header("(3) SIS (res:10min)")
    file_sis = path.replace('\\', '/') + '/Summary_Plot/Solar-Orbit/EPD/sis/' + str(select_day.year) + '/sis_ion_' + name + '.png'
    if os.path.isfile(file_sis):
        st.image(Image.open(file_sis))
    else:
        st.write('N/A')
with col2:
    st.header("(4) HET (res:10min)")
    file_het = path.replace('\\', '/') + '/Summary_Plot/Solar-Orbit/EPD/het/' + str(select_day.year) + '/het_ion_electron_' + name + '.png'
    if os.path.isfile(file_het):
        st.image(Image.open(file_het))
    else:
        st.write('N/A')
st.write("PS: A black colorbar and a black spectrum stand for one data point detected; \n "
         "a black colorbar and an empty spectrum stand for no data point detected")
st.header("(5)STIX")
file_stix = path.replace('\\', '/') + '/Summary_Plot/Solar-Orbit/STIX/STIX-LC/' + str(select_day.year) + '/stix_lightcurve_' + name + '.png'
if os.path.isfile(file_stix):
    st.image(Image.open(file_stix))
else:
    st.write('N/A')

st.header('2. WIND')
col1, col2 = st.columns(2)
with col1:
    st.header("(1) 0-1 (res:3min)")
    file_3dp_01 = path.replace('\\', '/') + '/Summary_Plot/WIND/3dp/' + str(select_day.year) + '/WIND_3dp_01_' + name + '.png'
    if os.path.isfile(file_3dp_01):
        st.image(Image.open(file_3dp_01))
    else:
        st.write('N/A')
with col2:
    st.header("(2) 6-7 (res:3min)")
    file_3dp_67 = path.replace('\\', '/') + '/Summary_Plot/WIND/3dp/' + str(select_day.year) + '/WIND_3dp_67_' + name + '.png'
    if os.path.isfile(file_3dp_67):
        st.image(Image.open(file_3dp_67))
    else:
        st.write('N/A')
col1, col2 = st.columns(2)
with col1:
    st.header("(3) pm_mfi (res:3min)")
    file_sol_wind = path.replace('\\', '/') + '/Summary_Plot/WIND/mfi_pm/' + str(select_day.year) + '/WIND_mfi_pm_' + name + '.png'
    if os.path.isfile(file_sol_wind):
        st.image(Image.open(file_sol_wind))
    else:
        st.write('N/A')
with col2:
    st.header("(4) PAD (res:3min)")
    file_wind_pad = path.replace('\\', '/') + '/Summary_Plot/WIND/3dp/' + str(select_day.year) + '/WIND_3dp_PAD_' + name + '.png'
    if os.path.isfile(file_wind_pad):
        st.image(Image.open(file_wind_pad))
    else:
        st.write('N/A')

st.header('3. Orbit (Weekly)')
first_day_of_year = Time(start_time.isot[0:4] + '-01-01T00:00:00.000', format='isot', scale='utc')
week_num = (start_time.jd - first_day_of_year.jd) // 7
name1_jd = first_day_of_year.jd + week_num * 7
name2_jd = first_day_of_year.jd + (week_num + 1) * 7
name1_Time = Time(name1_jd, format='jd', scale='utc')
name2_Time = Time(name2_jd, format='jd', scale='utc')
name1_str = name1_Time.isot[0:4] + name1_Time.isot[5:7] + name1_Time.isot[8:10]
name2_str = name2_Time.isot[0:4] + name2_Time.isot[5:7] + name2_Time.isot[8:10]
file_orbit = path.replace('\\', '/') + '/Summary_Plot/Planet_Orbit/' + str(select_day.year) + '/solo_planet_orbit_1_week_' + name1_str + 'T' \
             + name2_str + '.png'
if os.path.isfile(file_orbit):
    st.image(Image.open(file_orbit))
else:
    st.write('N/A')
