dvc run -n my_stage \
        -d src/get_df.py \
        -o data/df.csv \
        python src/get_df.py
