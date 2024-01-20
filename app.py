import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns


st.sidebar.title("Whatsap Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df=preprocessor.preprocess(data)

    st.dataframe(df)

    # fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("Show analysis Wrt",user_list)

    if st.sidebar.button("Show Analysis"):
        # stats
        num_media_messages,num_messages, num_links, words = helper.fetch_stats(selected_user,df)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total Words")
            st.title(words)

        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)

        with col4:
            st.header("Total Links")
            st.title(num_links)

        #timeline

        # Monthly Timeline
        st.title(" Monthly Timeline" )
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'],color='green')
        plt.xticks(rotation="vertical")
        st.pyplot(fig)

        #Daily_Timeline
        st.title(" Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation="vertical")
        st.pyplot(fig)

        # Activity Map
        st.title("Activity Map")
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most busy Day")
            busy_day = helper.week_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values)
            st.pyplot(fig)
        with col2:
            st.header("Most busy Month")
            busy_month = helper.month_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color="orange")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user,df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)






        # Finding the busiest person/user in the group
        if selected_user == "Overall":
            st.title('Most Busy Users')
            x, new_df =helper.most_busy_users(df)
            fig, ax = plt.subplots()


            col1,col2 = st.columns(2)


            with col1:
                ax.bar(x.index, x.values, color='Blue')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)
    # Word Cloud
        st.title("WordCloud:")
        df_wc = helper.create_wordcloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # Most Common Words
        st.title(" Most Common Words:")
        most_common_df = helper.most_common_words(selected_user,df)
        st.dataframe(most_common_df)

        st.title(" Most Common Words in Graph Form:")
        most_common_df = helper.most_common_words(selected_user, df)
        fig,ax = plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)









