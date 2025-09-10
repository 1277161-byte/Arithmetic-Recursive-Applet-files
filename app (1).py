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

def calculate_arithmetic_sum(first_term, common_difference, num_terms):
    """Calculate sum using the arithmetic series formula"""
    return (num_terms / 2) * (2 * first_term + (num_terms - 1) * common_difference)

def generate_geometric_sequence(first_term, common_ratio, num_terms):
    """Generate geometric sequence terms"""
    terms = []
    for n in range(1, num_terms + 1):
        term = first_term * (common_ratio ** (n - 1))
        terms.append(term)
    return terms

def calculate_geometric_sum(first_term, common_ratio, num_terms):
    """Calculate sum using the geometric series formula"""
    if common_ratio == 1:
        return num_terms * first_term
    else:
        return first_term * (1 - common_ratio ** num_terms) / (1 - common_ratio)

def main():
    st.title("📊 Sequence Explorer")
    st.markdown("### Learn about arithmetic and geometric sequences with interactive visualization!")
    
    # Sidebar for sequence type selection
    st.sidebar.header("Sequence Type")
    sequence_type = st.sidebar.radio(
        "Choose sequence type:",
        ["Arithmetic", "Geometric"],
        help="Select whether to explore arithmetic or geometric sequences"
    )
    
    # Sidebar for inputs
    st.sidebar.header("Sequence Parameters")
    
    # Common input - first term
    first_term = st.sidebar.number_input(
        "First Term (a₁)", 
        value=1.0,
        help="The first term of the sequence"
    )
    
    # Conditional inputs based on sequence type
    if sequence_type == "Arithmetic":
        second_param = st.sidebar.number_input(
            "Common Difference (d)", 
            value=2.0,
            help="The constant difference between consecutive terms"
        )
        param_name = "d"
        param_symbol = "d"
    else:  # Geometric
        second_param = st.sidebar.number_input(
            "Common Ratio (r)", 
            value=2.0,
            help="The constant ratio between consecutive terms"
        )
        param_name = "r"
        param_symbol = "r"
    
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
    
    # Generate sequence based on type
    if sequence_type == "Arithmetic":
        sequence = generate_arithmetic_sequence(first_term, second_param, int(num_terms))
        sum_value = calculate_arithmetic_sum(first_term, second_param, int(num_terms))
    else:  # Geometric
        sequence = generate_geometric_sequence(first_term, second_param, int(num_terms))
        sum_value = calculate_geometric_sum(first_term, second_param, int(num_terms))
    
    # Display formulas section
    st.header("📝 Formulas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("General Term Formula")
        if sequence_type == "Arithmetic":
            st.latex(r"a_n = a_1 + (n-1)d")
            st.markdown(f"""
            Where:
            - **a₁** = {first_term} (first term)
            - **d** = {second_param} (common difference)
            - **n** = term position
            """)
        else:  # Geometric
            st.latex(r"a_n = a_1 \cdot r^{n-1}")
            st.markdown(f"""
            Where:
            - **a₁** = {first_term} (first term)
            - **r** = {second_param} (common ratio)
            - **n** = term position
            """)
    
    with col2:
        st.subheader("Sum of First n Terms")
        if sequence_type == "Arithmetic":
            st.latex(r"S_n = \frac{n}{2}[2a_1 + (n-1)d]")
        else:  # Geometric
            if second_param == 1:
                st.latex(r"S_n = n \cdot a_1 \text{ (when } r = 1\text{)}")
            else:
                st.latex(r"S_n = a_1 \cdot \frac{1 - r^n}{1 - r} \text{ (when } r \neq 1\text{)}")
        
        st.markdown(f"""
        For **n = {int(num_terms)}** terms:
        
        **S₍{int(num_terms)}₎ = {sum_value:.6g}**
        """)
    
    # Display sequence terms
    st.header("🔢 Sequence Terms")
    
    # Show terms in a nice format
    terms_text = ", ".join([f"{term:.6g}" for term in sequence])
    st.markdown(f"**Terms:** {terms_text}")
    
    # Create detailed table for educational purposes
    if num_terms <= 20:  # Only show table for reasonable number of terms
        st.subheader("Term Details")
        term_data = []
        for i, term in enumerate(sequence, 1):
            if sequence_type == "Arithmetic":
                calculation = f"{first_term} + ({i}-1)×{second_param} = {term:.6g}"
            else:  # Geometric
                calculation = f"{first_term} × {second_param}^({i}-1) = {term:.6g}"
            
            term_data.append({
                "Position (n)": i,
                "Calculation": calculation,
                "Value (aₙ)": f"{term:.6g}"
            })
        
        st.dataframe(term_data, width='stretch')
    
    # Visualization
    st.header("📈 Visualization")
    
    # Create matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot the sequence
    positions = list(range(1, len(sequence) + 1))
    if sequence_type == "Arithmetic":
        ax.plot(positions, sequence, 'bo-', linewidth=2, markersize=8, label='Arithmetic Sequence')
        title = f'Arithmetic Sequence: a₁={first_term}, d={second_param}'
    else:  # Geometric
        ax.plot(positions, sequence, 'ro-', linewidth=2, markersize=8, label='Geometric Sequence')
        title = f'Geometric Sequence: a₁={first_term}, r={second_param}'
    
    # Customize the plot
    ax.set_xlabel('Term Position (n)', fontsize=12)
    ax.set_ylabel('Term Value (aₙ)', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    # Add value labels on points (only if not too many terms and values aren't too large)
    if num_terms <= 20 and max(abs(val) for val in sequence) < 1000:
        for i, (x, y) in enumerate(zip(positions, sequence)):
            ax.annotate(f'{y:.3g}', (x, y), textcoords="offset points", xytext=(0,10), ha='center')
    
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
        if sequence_type == "Arithmetic":
            st.metric("Common Difference", f"{second_param}")
        else:
            st.metric("Common Ratio", f"{second_param}")
        
    with col3:
        st.metric("Sum of All Terms", f"{sum_value:.6g}")
    
    # Additional information
    st.markdown("---")
    
    if sequence_type == "Arithmetic":
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
    else:  # Geometric
        st.markdown("""
        ### 📚 About Geometric Sequences
        
        A **geometric sequence** is a sequence of numbers where each term after the first is obtained by multiplying the previous term by a constant value (called the common ratio).
        
        **Key Properties:**
        - The ratio between consecutive terms is constant
        - The general term can be expressed as: aₙ = a₁ × r^(n-1)
        - The sum of the first n terms follows the formula: Sₙ = a₁ × (1-r^n)/(1-r) when r ≠ 1
        - When r = 1, the sum is simply: Sₙ = n × a₁
        
        **Examples in Real Life:**
        - Population growth (doubling every generation)
        - Compound interest in banking
        - Radioactive decay (half-life)
        - Viral spread patterns
        """)

if __name__ == "__main__":
    main()