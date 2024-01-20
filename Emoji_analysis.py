"""
        # Emoji Analysis
        emoji_df = helper.emoji_helper(selected_user,df)
        st.title("Emoji Analysis")

        columns = st.beta_columns(2)
        if columns is not None and len(columns) == 2:
            col1, col2 = columns
            with col1:
                st.dataframe(emoji_df)

            # with col2:
            # fig.ax=plt.subplots()
            # ax.pie(emoji_df[0],emoji_df[1])
            # st.pyplot(fig)
            with col2:
                fig, ax = plt.subplots()
                ax.pie(emoji_df[1], labels=emoji_df[0], autopct='%1.1f%%', startangle=90)
                st.pyplot(fig)
        else:
            st.error("Failed to create columns.")

        # col1, col2 = st.beta_columns(2)
        """
