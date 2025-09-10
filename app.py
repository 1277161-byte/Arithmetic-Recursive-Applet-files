import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def generate_arithmetic_sequence(first_term, common_difference, num_terms):
    """Generate arithmetic sequence terms"""
    terms = []
    for n in range(1, num_terms + 1):
        term = first_term + (n - 1) * common_difference
        terms.append(term)
    return terms

def calculate_sum_formula(first_term, common_difference, num_terms):
    """Calculate sum using the arithmetic series formula"""
    return (num_terms / 2) * (2 * first_term + (num_terms - 1) * common_difference)

def main():
    st.title("📊 Arithmetic Sequence Explorer")
    st.markdown("### Learn about arithmetic sequences with interactive visualization!")
    
    # Sidebar for inputs
    st.sidebar.header("Sequence Parameters")
    
    # Input fields with validation
    first_term = st.sidebar.number_input(
        "First Term (a₁)", 
        value=1.0,
        help="The first term of the arithmetic sequence"
    )
    
    common_difference = st.sidebar.number_input(
        "Common Difference (d)", 
        value=2.0,
        help="The constant difference between consecutive terms"
    )
    
    num_terms = st.sidebar.number_input(
        "Number of Terms (n)", 
        min_value=1, 
        max_value=100, 
        value=10,
        step=1,
        help="How many terms to generate (maximum 100)"
    )
    
    # Validate inputs
    if num_terms <= 0:
        st.error("Number of terms must be a positive integer!")
        return
    
    # Generate sequence
    sequence = generate_arithmetic_sequence(first_term, common_difference, int(num_terms))
    
    # Display formulas section
    st.header("📝 Formulas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("General Term Formula")
        st.latex(r"a_n = a_1 + (n-1)d")
        st.markdown(f"""
        Where:
        - **a₁** = {first_term} (first term)
        - **d** = {common_difference} (common difference)
        - **n** = term position
        """)
    
    with col2:
        st.subheader("Sum of First n Terms")
        st.latex(r"S_n = \frac{n}{2}[2a_1 + (n-1)d]")
        sum_value = calculate_sum_formula(first_term, common_difference, int(num_terms))
        st.markdown(f"""
        For **n = {int(num_terms)}** terms:
        
        **S₁₀ = {sum_value}**
        """)
    
    # Display sequence terms
    st.header("🔢 Sequence Terms")
    
    # Show terms in a nice format
    terms_text = ", ".join([f"{term}" for term in sequence])
    st.markdown(f"**Terms:** {terms_text}")
    
    # Create detailed table for educational purposes
    if num_terms <= 20:  # Only show table for reasonable number of terms
        st.subheader("Term Details")
        term_data = []
        for i, term in enumerate(sequence, 1):
            calculation = f"{first_term} + ({i}-1)×{common_difference} = {term}"
            term_data.append({
                "Position (n)": i,
                "Calculation": calculation,
                "Value (aₙ)": term
            })
        
        st.dataframe(term_data, use_container_width=True)
    
    # Visualization
    st.header("📈 Visualization")
    
    # Create matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot the sequence
    positions = list(range(1, len(sequence) + 1))
    ax.plot(positions, sequence, 'bo-', linewidth=2, markersize=8, label='Arithmetic Sequence')
    
    # Customize the plot
    ax.set_xlabel('Term Position (n)', fontsize=12)
    ax.set_ylabel('Term Value (aₙ)', fontsize=12)
    ax.set_title(f'Arithmetic Sequence: a₁={first_term}, d={common_difference}', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    # Add value labels on points
    for i, (x, y) in enumerate(zip(positions, sequence)):
        ax.annotate(f'{y}', (x, y), textcoords="offset points", xytext=(0,10), ha='center')
    
    # Set integer ticks for x-axis if reasonable number of terms
    if num_terms <= 20:
        ax.set_xticks(positions)
    
    st.pyplot(fig)
    
    # Mathematical insights
    st.header("🧮 Mathematical Insights")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("First Term", f"{first_term}")
        
    with col2:
        st.metric("Common Difference", f"{common_difference}")
        
    with col3:
        st.metric("Sum of All Terms", f"{sum_value}")
    
    # Additional information
    st.markdown("---")
    st.markdown("""
    ### 📚 About Arithmetic Sequences
    
    An **arithmetic sequence** is a sequence of numbers where each term after the first is obtained by adding a constant value (called the common difference) to the previous term.
    
    **Key Properties:**
    - The difference between consecutive terms is constant
    - The general term can be expressed as: aₙ = a₁ + (n-1)d
    - The sum of the first n terms follows the formula: Sₙ = n/2 × [2a₁ + (n-1)d]
    
    **Examples in Real Life:**
    - Saving money regularly (e.g., $50 each month)
    - Temperature changes at regular intervals
    - Seating arrangements in theaters
    """)

if __name__ == "__main__":
    main()
