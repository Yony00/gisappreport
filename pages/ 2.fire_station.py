st.set_page_config(layout="wide")
st.title("臺南市各消防局統計資料")
st.header("臺南市各消防局點位")
st.markdown(markdown)

polygon = 'https://github.com/.../TOWN_MOI_1131028.shp'
taiwan = gpd.read_file(polygon)
tainan = taiwan[taiwan['COUNTYNAME'] == '臺南市']

firestation_point_csv = 'https://raw.githubusercontent.com/tim9810/gis_final_exam/refs/heads/main/%E5%8F%B0%E5%8D%97%E6%B6%88%E9%98%B2%E5%B1%80wgs84%E5%BA%A7%E6%A8%99utf.csv'
firestation_point = pd.read_csv(firestation_point_csv)

option_list = hospital_point["行政區"].unique().tolist()
option = st.multiselect("選擇行政區", option_list)
filtered = hospital_point[hospital_point["行政區"].isin(option)]

m = leafmap.Map(center=[23, 120.3], zoom=10)
m.add_points_from_xy(
    filtered, x='经度', y='纬度',
    popup=['地址'],
    layer_name="消防局點位",
)
m.to_streamlit(height=400)

st.dataframe(filtered) 

