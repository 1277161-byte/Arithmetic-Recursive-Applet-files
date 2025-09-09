import streamlit as st

def generate_arithmetic_sequence(first_term, common_difference, num_terms):
    return [first_term + i * common_difference for i in range(num_terms)]

def main():
    st.title("Arithmetic Sequence Generator")

    st.write("Enter the values below to generate an arithmetic sequence:")

    # Inputs
    a1 = st.number_input("First term (a₁):", value=1)
    d = st.number_input("Common difference (d):", value=1)
    n = st.number_input("Number of terms (n):", min_value=1, value=10)

    if st.button("Generate Sequence"):
        sequence = generate_arithmetic_sequence(a1, d, n)
        st.subheader("Generated Sequence:")
        st.write(sequence)

if __name__ == "__main__":
    main()
streamlit
