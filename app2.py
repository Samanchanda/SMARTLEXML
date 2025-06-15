import streamlit as st
from backend_model import *
from PIL import Image

# Enhanced Dark Theme with Vibrant Colors
st.markdown("""
<style>
    :root {
        --primary: #6e48aa;
        --secondary: #9d50bb;
        --accent: #4776E6;
        --success: #2ecc71;
        --warning: #f39c12;
        --danger: #e74c3c;
        --info: #3498db;
        --text: #f0f2f6;
        --bg-dark: #0e1117;
        --bg-card: #1e2130;
    }

    .stApp {
        background-color: var(--bg-dark);
        color: var(--text);
        background-image: radial-gradient(circle at 15% 50%, rgba(110, 72, 170, 0.1) 0%, rgba(0,0,0,0) 25%),
                          radial-gradient(circle at 85% 30%, rgba(157, 80, 187, 0.1) 0%, rgba(0,0,0,0) 25%);
    }

    .header-gradient {
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        border: none;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }

    .stTextArea textarea {
        background-color: var(--bg-card);
        color: var(--text);
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.3s;
    }

    .stTextArea textarea:focus {
        border-color: var(--accent);
        box-shadow: 0 0 0 2px rgba(71, 118, 230, 0.2);
    }

    .stButton>button {
        background: linear-gradient(135deg, var(--primary), var(--accent));
        color: white;
        border-radius: 12px;
        padding: 12px 28px;
        font-weight: bold;
        border: none;
        transition: all 0.3s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 7px 14px rgba(110, 72, 170, 0.3);
    }

    .stRadio>div {
        background-color: var(--bg-card);
        border-radius: 12px;
        padding: 12px;
        border: 1px solid rgba(255,255,255,0.1);
    }

    .metric-card {
        background-color: var(--bg-card);
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        border-left: 6px solid;
        transition: transform 0.3s;
    }

    .metric-card:hover {
        transform: translateY(-5px);
    }

    .success-card {
        border-left-color: var(--success);
        background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), var(--bg-card));
    }

    .warning-card {
        border-left-color: var(--warning);
        background: linear-gradient(135deg, rgba(243, 156, 18, 0.1), var(--bg-card));
    }

    .danger-card {
        border-left-color: var(--danger);
        background: linear-gradient(135deg, rgba(231, 76, 60, 0.1), var(--bg-card));
    }

    .st-expander {
        background-color: var(--bg-card);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 12px;
    }

    .stDataFrame {
        background-color: var(--bg-card);
        border-radius: 12px;
    }

    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: var(--text);
    }

    .uploaded-image {
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.1);
        margin: 15px 0;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }

    .risk-high {
        background: linear-gradient(135deg, var(--danger), #c0392b);
        color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(231, 76, 60, 0.3);
    }

    .risk-medium {
        background: linear-gradient(135deg, var(--warning), #e67e22);
        color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(243, 156, 18, 0.3);
    }

    .risk-low {
        background: linear-gradient(135deg, var(--success), #27ae60);
        color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(46, 204, 113, 0.3);
    }

    .tab-content {
        padding: 20px;
        background-color: var(--bg-card);
        border-radius: 0 0 12px 12px;
        border: 1px solid rgba(255,255,255,0.1);
        border-top: none;
    }

    .reference-badge {
        display: inline-block;
        background: rgba(71, 118, 230, 0.2);
        color: var(--accent);
        padding: 4px 8px;
        border-radius: 6px;
        font-size: 0.8em;
        margin: 5px 0;
        border-left: 3px solid var(--accent);
    }

    .pulse-animation {
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    .floating {
        animation: floating 3s ease-in-out infinite;
    }

    @keyframes floating {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
</style>
""", unsafe_allow_html=True)

# Initialize database and model
init_db()
model, tokenizer, device = load_model()

# Header section with enhanced design
st.markdown("""
<div class="header-gradient floating">
    <h1 style="color: white; margin: 0; text-align: center; font-size: 2.5em;">🦸‍♂️ SMARTLEXML 🦸‍♀️</h1>
    <p style="color: rgba(255,255,255,0.9); text-align: center; font-size: 1.2em; margin-top: 10px;">
    AI-powered Contract Risk Assessment with Legal References</p>
</div>
""", unsafe_allow_html=True)

# How to Use section with icon animation
st.markdown("""
<div style="background-color: #1e2130; color: #f0f2f6; padding: 20px; border-radius: 12px; 
            margin-bottom: 25px; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 5px 15px rgba(0,0,0,0.2);">
    <h3 style="color: #6e48aa; margin: 0 0 15px 0; display: flex; align-items: center;">
        <span style="margin-right: 10px;">📌</span> How to Use
    </h3>
    <ol style="margin: 10px 0 0 20px; padding: 0; color: #f0f2f6; line-height: 1.6;">
        <li style="margin-bottom: 8px;">Paste contract text <strong style="color: #9d50bb;">OR</strong> Upload image of contract (PNG/JPG)</li>
        <li style="margin-bottom: 8px;">The system will automatically process the content</li>
        <li style="margin-bottom: 8px;">Click <span style="color: #4776E6; font-weight: bold;">Analyze Contract</span> button</li>
        <li style="margin-bottom: 8px;">View detailed risk analysis with <span style="color: #2ecc71;">legal references</span></li>
        <li>All reports are saved to database for future reference</li>
    </ol>
</div>
""", unsafe_allow_html=True)

# Input method with better styling
input_method = st.radio(
    "Input Method:",
    ["Text Input", "Image Upload"],
    horizontal=True,
    label_visibility="collapsed"
)

if input_method == "Text Input":
    contract_text = st.text_area(
        "📝 Paste contract here:",
        height=300,
        placeholder="Enter your contract text here...\n\nThe system will analyze for:\n- Ambiguous terms\n- Unenforceable clauses\n- Missing sections\n- Risk assessment",
        help="Paste the full contract text you want to analyze"
    )
else:
    uploaded_file = st.file_uploader(
        "📤 Upload Contract Image",
        type=["png", "jpg", "jpeg"],
        help="Upload a clear image of your contract document for text extraction"
    )
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Contract", use_container_width=True, output_format="PNG",
                 width=300, clamp=True)
        contract_text = extract_text_from_image(image)
        contract_text = st.text_area(
            "✍️ Extracted Text (edit if needed):",
            value=contract_text,
            height=300
        )

if st.button("🚀 Analyze Contract", type="primary", key="analyze_btn") and contract_text:
    with st.spinner("🔍 Analyzing contract... This may take a moment"):
        analysis = analyze_contract(contract_text, model, tokenizer, device)
        save_to_db(analysis)

        st.success("✅ Analysis Complete!")
        st.balloons()


        # Results section with enhanced design
        st.markdown("""
        <div style="background: linear-gradient(135deg, #1a1d2c, #2c3e50); color: #6e48aa; 
                    padding: 15px 20px; border-radius: 12px; margin: 25px 0; 
                    border: 1px solid rgba(110, 72, 170, 0.3); box-shadow: 0 8px 16px rgba(0,0,0,0.3);">
            <h2 style="color: white; margin: 0; display: flex; align-items: center;">
                <span style="margin-right: 10px;">📜</span> Contract Analysis Report
            </h2>
        </div>
        """, unsafe_allow_html=True)

        # Metrics in columns with hover effects
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class="metric-card {'danger-card' if analysis.get('risk_score', 0) > 60 else 'warning-card' if analysis.get('risk_score', 0) > 30 else 'success-card'} pulse-animation">
                <h3 style="margin: 0 0 10px 0; color: #f0f2f6;">Risk Score</h3>
                <h1 style="margin: 0; color: {'#e74c3c' if analysis.get('risk_score', 0) > 60 else '#f39c12' if analysis.get('risk_score', 0) > 30 else '#2ecc71'}">
                    {analysis.get('risk_score', 0)}/100</h1>
                <p style="margin: 5px 0 0 0; font-size: 0.9em; color: rgba(240,242,246,0.7);">
                    {'High risk' if analysis.get('risk_score', 0) > 60 else 'Moderate risk' if analysis.get('risk_score', 0) > 30 else 'Low risk'}
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="metric-card {'success-card' if analysis.get('clause_class', 1) == 1 else 'danger-card'}">
                <h3 style="margin: 0 0 10px 0; color: #f0f2f6;">Classification</h3>
                <h1 style="margin: 0; color: {'#e74c3c' if analysis.get('clause_class', 1) == 0 else '#2ecc71'}">
                    {'✅ Valid' if analysis.get('clause_class', 1) == 1 else '⚠️ Risky'}
                </h1>
                <p style="margin: 5px 0 0 0; font-size: 0.9em; color: rgba(240,242,246,0.7);">
                    {'Low dispute risk' if analysis.get('clause_class', 1) == 1 else 'Potential legal risks'}
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="metric-card {'danger-card' if analysis.get('contract_strength') == 'Weak' else 'warning-card' if analysis.get('contract_strength') == 'Moderate' else 'success-card'}">
                <h3 style="margin: 0 0 10px 0; color: #f0f2f6;">Contract Strength</h3>
                <h1 style="margin: 0; color: {'#e74c3c' if analysis.get('contract_strength') == 'Weak' else '#f39c12' if analysis.get('contract_strength') == 'Moderate' else '#2ecc71'}">
                    {analysis.get('contract_strength', 'Unknown')}
                </h1>
                <p style="margin: 5px 0 0 0; font-size: 0.9em; color: rgba(240,242,246,0.7);">
                    {'Needs review' if analysis.get('contract_strength') == 'Weak' else 'Could be stronger' if analysis.get('contract_strength') == 'Moderate' else 'Strong enforceability'}
                </p>
            </div>
            """, unsafe_allow_html=True)

        # Findings in tabs with better organization
        tab1, tab2, tab3, tab4 = st.tabs(["🔍 Ambiguities", "⚠️ Red Flags", "📊 Language Analysis", "🔎 Missing Sections"])

        with tab1:
            ambiguities = analysis.get('ambiguities', {})
            if ambiguities:
                st.markdown('<div class="tab-content">', unsafe_allow_html=True)
                st.markdown("""
                <div style="margin-bottom: 15px; padding: 10px; background: rgba(231, 76, 60, 0.1); 
                            border-radius: 8px; border-left: 4px solid #e74c3c;">
                    <h4 style="margin: 0 0 5px 0; color: #f0f2f6;">⚠️ Vague Language Detected</h4>
                    <p style="margin: 0; color: rgba(240,242,246,0.7); font-size: 0.9em;">
                        These terms are frequently disputed in court
                    </p>
                </div>
                """, unsafe_allow_html=True)

                for term, data in ambiguities.items():
                    st.markdown(f"""
                    <div style="margin: 10px 0; padding: 15px; background: rgba(30, 33, 48, 0.8); 
                                border-radius: 8px; border-left: 4px solid #9d50bb;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <h4 style="margin: 0; color: #f0f2f6;">{term.capitalize()}</h4>
                            <span style="background: #e74c3c; color: white; padding: 3px 8px; border-radius: 12px; 
                                        font-size: 0.8em;">{data.get('count', 0)} found</span>
                        </div>
                        <div class="reference-badge" style="margin-top: 8px;">
                            {data.get('reference', '')}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style="padding: 20px; background: rgba(46, 204, 113, 0.1); border-radius: 8px; 
                            text-align: center; border: 1px dashed rgba(46, 204, 113, 0.5);">
                    <h4 style="margin: 0; color: #2ecc71;">✅ No Ambiguous Terms Found</h4>
                    <p style="margin: 5px 0 0 0; color: rgba(46, 204, 113, 0.8);">
                        The contract language appears precise and enforceable
                    </p>
                </div>
                """, unsafe_allow_html=True)

        with tab2:
            fake_indicators = analysis.get('fake_indicators', {})
            if fake_indicators:
                st.markdown('<div class="tab-content">', unsafe_allow_html=True)
                st.markdown("""
                <div style="margin-bottom: 15px; padding: 10px; background: rgba(231, 76, 60, 0.1); 
                            border-radius: 8px; border-left: 4px solid #e74c3c;">
                    <h4 style="margin: 0 0 5px 0; color: #f0f2f6;">🚨 High-Risk Indicators</h4>
                    <p style="margin: 0; color: rgba(240,242,246,0.7); font-size: 0.9em;">
                        These clauses may render the contract unenforceable
                    </p>
                </div>
                """, unsafe_allow_html=True)

                for term, data in fake_indicators.items():
                    st.markdown(f"""
                    <div style="margin: 10px 0; padding: 15px; background: rgba(30, 33, 48, 0.8); 
                                border-radius: 8px; border-left: 4px solid #e74c3c;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <h4 style="margin: 0; color: #f0f2f6;">{term.capitalize()}</h4>
                            <span style="background: #e74c3c; color: white; padding: 3px 8px; border-radius: 12px; 
                                        font-size: 0.8em;">{data.get('count', 0)} found</span>
                        </div>
                        <div class="reference-badge" style="margin-top: 8px;">
                            {data.get('reference', '')}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style="padding: 20px; background: rgba(46, 204, 113, 0.1); border-radius: 8px; 
                            text-align: center; border: 1px dashed rgba(46, 204, 113, 0.5);">
                    <h4 style="margin: 0; color: #2ecc71;">✅ No Red Flags Found</h4>
                    <p style="margin: 5px 0 0 0; color: rgba(46, 204, 113, 0.8);">
                        No significant enforceability issues detected
                    </p>
                </div>
                """, unsafe_allow_html=True)

        with tab3:
            modals = analysis.get('modals', {})
            if modals:
                st.markdown('<div class="tab-content">', unsafe_allow_html=True)
                st.markdown("""
                <div style="margin-bottom: 15px; padding: 10px; background: rgba(52, 152, 219, 0.1); 
                            border-radius: 8px; border-left: 4px solid #3498db;">
                    <h4 style="margin: 0 0 5px 0; color: #f0f2f6;">📝 Language Analysis</h4>
                    <p style="margin: 0; color: rgba(240,242,246,0.7); font-size: 0.9em;">
                        Modal verbs and their legal implications
                    </p>
                </div>
                """, unsafe_allow_html=True)

                for verb, data in modals.items():
                    weight_color = "#e74c3c" if data.get('weight', 0) >= 0.4 else "#f39c12" if data.get('weight',
                                                                                                        0) >= 0.2 else "#2ecc71"
                    st.markdown(f"""
                    <div style="margin: 10px 0; padding: 15px; background: rgba(30, 33, 48, 0.8); 
                                border-radius: 8px; border-left: 4px solid #3498db;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <h4 style="margin: 0; color: #f0f2f6;">{verb.capitalize()}</h4>
                            <div>
                                <span style="background: {weight_color}; color: white; padding: 3px 8px; 
                                          border-radius: 12px; font-size: 0.8em;">
                                    {data.get('count', 0)} occurrences
                                </span>
                            </div>
                        </div>
                        <div style="margin-top: 10px;">
                            <div style="background: rgba(52, 152, 219, 0.2); height: 6px; border-radius: 3px; 
                                        width: 100%; margin-bottom: 5px;">
                                <div style="background: {weight_color}; height: 6px; border-radius: 3px; 
                                            width: {data.get('weight', 0) * 100}%;"></div>
                            </div>
                            <div class="reference-badge" style="margin-top: 5px;">
                                {data.get('reference', '')}
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style="padding: 20px; background: rgba(52, 152, 219, 0.1); border-radius: 8px; 
                            text-align: center; border: 1px dashed rgba(52, 152, 219, 0.5);">
                    <h4 style="margin: 0; color: #3498db;">ℹ️ No Significant Modal Verbs</h4>
                    <p style="margin: 5px 0 0 0; color: rgba(52, 152, 219, 0.8);">
                        The contract doesn't contain many modal verbs that affect risk
                    </p>
                </div>
                """, unsafe_allow_html=True)

        with tab4:
            missing_sections = analysis.get('missing_sections', [])
            if missing_sections:
                st.markdown('<div class="tab-content">', unsafe_allow_html=True)
                st.markdown("""
                <div style="margin-bottom: 15px; padding: 10px; background: rgba(231, 76, 60, 0.1); 
                            border-radius: 8px; border-left: 4px solid #e74c3c;">
                    <h4 style="margin: 0 0 5px 0; color: #f0f2f6;">⚠️ Essential Sections Missing</h4>
                    <p style="margin: 0; color: rgba(240,242,246,0.7); font-size: 0.9em;">
                        These sections are recommended by ABA Model Rules
                    </p>
                </div>
                """, unsafe_allow_html=True)

                for section in missing_sections:
                    st.markdown(f"""
                    <div style="margin: 10px 0; padding: 15px; background: rgba(30, 33, 48, 0.8); 
                                border-radius: 8px; border-left: 4px solid #e74c3c;">
                        <h4 style="margin: 0 0 5px 0; color: #f0f2f6;">{section.get('section', '').capitalize()}</h4>
                        <div class="reference-badge">
                            {section.get('reference', '')}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style="padding: 20px; background: rgba(46, 204, 113, 0.1); border-radius: 8px; 
                            text-align: center; border: 1px dashed rgba(46, 204, 113, 0.5);">
                    <h4 style="margin: 0; color: #2ecc71;">✅ All Essential Sections Present</h4>
                    <p style="margin: 5px 0 0 0; color: rgba(46, 204, 113, 0.8);">
                        The contract contains all standard sections recommended by ABA
                    </p>
                </div>
                """, unsafe_allow_html=True)

        # Recommendations with better organization
        st.markdown("""
        <div style="background-color: #1e2130; padding: 20px; border-radius: 12px; margin: 25px 0; 
                    border: 1px solid rgba(110, 72, 170, 0.3); box-shadow: 0 5px 15px rgba(0,0,0,0.2);">
            <h3 style="color: #6e48aa; margin: 0 0 15px 0; display: flex; align-items: center;">
                <span style="margin-right: 10px;">💡</span> Legal Recommendations
            </h3>
        """, unsafe_allow_html=True)

        if analysis['risk_score'] > 60:
            st.markdown("""
            <div class="risk-high">
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <span style="font-size: 1.5em; margin-right: 10px;">🚨</span>
                    <h4 style="margin: 0;">Critical Risk Detected</h4>
                </div>
                <p style="margin: 0;">This contract requires <strong>substantial legal review</strong> before signing. Multiple high-risk elements detected that could lead to disputes or unenforceability.</p>
                <div style="margin-top: 15px; background: rgba(255,255,255,0.1); padding: 10px; border-radius: 8px;">
                    <p style="margin: 0; font-size: 0.9em;">🔹 Consult with a contract attorney<br>
                    🔹 Request modifications for ambiguous terms<br>
                    🔹 Clarify or remove unenforceable clauses</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        elif analysis['risk_score'] > 30:
            st.markdown("""
            <div class="risk-medium">
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <span style="font-size: 1.5em; margin-right: 10px;">⚠️</span>
                    <h4 style="margin: 0;">Moderate Risk Detected</h4>
                </div>
                <p style="margin: 0;">Review highlighted issues with legal counsel. Some concerning elements need attention before signing.</p>
                <div style="margin-top: 15px; background: rgba(255,255,255,0.1); padding: 10px; border-radius: 8px;">
                    <p style="margin: 0; font-size: 0.9em;">🔹 Consider clarifying ambiguous language<br>
                    🔹 Verify missing sections aren't critical<br>
                    🔹 Assess if risk level is acceptable</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="risk-low">
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <span style="font-size: 1.5em; margin-right: 10px;">✅</span>
                    <h4 style="margin: 0;">Low Risk Detected</h4>
                </div>
                <p style="margin: 0;">Contract appears legally sound. Standard review recommended before signing.</p>
                <div style="margin-top: 15px; background: rgba(255,255,255,0.1); padding: 10px; border-radius: 8px;">
                    <p style="margin: 0; font-size: 0.9em;">🔹 Verify all parties understand terms<br>
                    🔹 Ensure proper execution procedures<br>
                    🔹 Store signed copy securely</p>
                </div>
            </div>
            """, unsafe_allow_html=True)


# History section with better design
if st.button("📁 View Analysis History", key="history_btn"):
    history = get_previous_analyses()
    if not history.empty:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #1a1d2c, #2c3e50); color: #6e48aa; 
                    padding: 15px 20px; border-radius: 12px; margin: 25px 0; 
                    border: 1px solid rgba(110, 72, 170, 0.3); box-shadow: 0 8px 16px rgba(0,0,0,0.3);">
            <h2 style="color: white; margin: 0; display: flex; align-items: center;">
                <span style="margin-right: 10px;">⏳</span> Previous Analyses
            </h2>
        </div>
        """, unsafe_allow_html=True)

        # Enhanced dataframe display
        st.dataframe(
            history,
            column_config={
                "timestamp": st.column_config.DatetimeColumn("Timestamp", format="DD MMM YYYY, h:mm a"),
                "classification": st.column_config.TextColumn("Status",
                                                              help="Contract classification status"),
                "risk_score": st.column_config.ProgressColumn(
                    "Risk Score",
                    help="Risk score from 0 to 100",
                    format="%.0f",
                    min_value=0,
                    max_value=100,
                ),
                "strength": st.column_config.TextColumn("Strength"),
                "text_length": st.column_config.NumberColumn("Text Length",
                                                             help="Number of characters in contract")
            },
            use_container_width=True,
            hide_index=True
        )


