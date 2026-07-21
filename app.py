import streamlit as st
st.title("N-Queens Problem using Backtracking")
n = st.slider("Select N", 4, 10, 4)
solutions, backtracks = solve_n_queens(n)
st.write("### Number of Solutions")
st.success(len(solutions))
st.write("### Number of Backtracks")
st.info(backtracks)
if st.checkbox("Show Solutions"):
    for i, sol in enumerate(solutions):
        st.write(f"Solution {i+1}")
        st.write(sol)
