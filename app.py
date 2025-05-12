import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Оценка стоимости КТС", layout="wide")

# --- Период расчета (отдельно сверху) ---
period_options = [
    "Последний месяц",
    "Последние 3 месяца",
    "Последние 6 месяцев",
    "Годовой диапазон",
    "Конкретный месяц"
]
selected_period = st.selectbox("Выберите период расчета", period_options)

if selected_period == "Годовой диапазон":
    start_year = st.number_input("Начало периода (год)", min_value=2010, max_value=datetime.now().year, value=datetime.now().year-1)
elif selected_period == "Конкретный месяц":
    selected_month = st.date_input("Выберите месяц", value=datetime.now())

st.divider()

# --- Основная форма в 2 колонки ---
col1, col2 = st.columns(2)

with col1:
# --- Марка автомобиля ---
    brand_options = ["ВАЗ"]
    brand = st.selectbox("Марка автомобиля", brand_options)

    # --- Модельная группа ---
    model_group_options = ["Lada Granta", "Lada Vesta", "Lada Niva"]
    model_group = st.selectbox("Модельная группа", model_group_options)

    # --- Модель транспортного средства ---
    model_name_options = ["Granta 1.6 AT", "Vesta SW Cross", "Niva Legend 4x4"]
    model_name = st.selectbox("Модель транспортного средства", model_name_options)

    # --- Регион ---
    region_options = ["Москва", "Санкт-Петербург", "Краснодарский край", "Волгоградская область", "Татарстан"]
    region = st.selectbox("Регион (область или город)", region_options)


with col2:
    probeg = st.number_input("Фактический пробег КТС (км)", min_value=0, step=1000, format="%d")
    current_year = datetime.now().year
    god_vypuska = st.number_input("Год выпуска КТС", min_value=1980, max_value=current_year, step=1)

    uslovie_options = {
        "Обычные (город/трасса)": 0,
        "Тяжелые (такси, бездорожье, грузовые)": -5,
        "Щадящие (редкое использование)": 2,
    }
    uslovie_label = st.selectbox("Условия эксплуатации", list(uslovie_options.keys()))

    Cdop_options = [
        "Корректировка за повреждения",
        "Корректировка за тюнинг",
        "Корректировка за разукомплектацию",
        "Корректировка за обновление составных частей",
        "Иное влияние на стоимость",
    ]
    Cdop_choice = st.selectbox("Дополнительная корректировка (Сдоп)", Cdop_options)


st.divider()

# --- Кнопка расчета ---
if st.button("🔍 Рассчитать стоимость КТС"):
    fake_price = 633000  # Здесь можно будет потом подставить реальный расчет

    st.success(f"Рассчитанная рыночная стоимость: {fake_price:,.0f} руб.".replace(',', ' '))
    
    st.write(f"Марка: {brand}")
    st.write(f"Модельная группа: {model_group}")
    st.write(f"Модель: {model_name}")
    st.write(f"Регион: {region}")
    st.write(f"Фактический пробег: {probeg} км")
    st.write(f"Год выпуска: {god_vypuska}")
    st.write(f"Условия эксплуатации: {uslovie_label}")
    st.write(f"Выбранная доп. корректировка: {Cdop_choice}")

