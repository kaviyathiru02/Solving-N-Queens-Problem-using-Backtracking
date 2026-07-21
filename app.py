import streamlit as st
def is_safe(board, row, col):
    for prev_row in range(row):
        placed = board[prev_row]
        if placed == col:
            return False
        if abs(prev_row - row) == abs(placed - col):
            return False
    return True
def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    backtrack_count = [0]
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
                backtrack_count[0] += 1
    backtrack(0)
    return solutions, backtrack_count[0]
def display_board(solution):
    n = len(solution)
    html = """
    <table style='border-collapse: collapse; margin-bottom:20px;'>
    """
    for i in range(n):
        html += "<tr>"
        for j in range(n):
            color = "#f0d9b5" if (i + j) % 2 == 0 else "#b58863"
            if solution[i] == j:
                cell = "♛"
                text_color = "red"
            else:
                cell = ""
                text_color = "black"
            html += f"""
            <td style="
                width:50px;
                height:50px;
                text-align:center;
                font-size:32px;
                background:{color};
                color:{text_color};
                border:1px solid black;">
                {cell}
            </td>
            """
        html += "</tr>"
    html += "</table>"
    st.markdown(html, unsafe_allow_html=True)
st.set_page_config(
    page_title="N-Queens Problem",
    page_icon="♛",
    layout="centered"
)
st.title("♛ N-Queens Problem using Backtracking")
st.write(
    """
Select the value of **N** to solve the N-Queens problem using the
**Backtracking Algorithm**.
"""
)
n = st.slider("Select N", 4, 8, 4)
solutions, backtracks = solve_n_queens(n)
st.success(f"Total Solutions: {len(solutions)}")
st.info(f"Backtracking Count: {backtracks}")
if st.checkbox("Show Solutions"):
    for i, solution in enumerate(solutions, start=1):
        st.subheader(f"Solution {i}")
        display_board(solution)
        st.write("Queen Positions:", solution)
st.markdown("---")
st.caption("Developed using Python and Streamlit")
