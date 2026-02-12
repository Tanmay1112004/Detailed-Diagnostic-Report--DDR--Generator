"""
DDR Report Generator - Applied AI Builder Assignment
Streamlit frontend with Gemini 2.5 Flash integration
Generates Detailed Diagnostic Report from Inspection + Thermal PDFs
"""

import streamlit as st
import PyPDF2
import google.generativeai as genai
from datetime import datetime
import io
import time

# ============================================
# PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="DDR Report Generator",
    page_icon="🏠",
    layout="wide"
)

# ============================================
# GEMINI CONFIGURATION
# ============================================
GEMINI_API_KEY = "Your_API_Key"
MODEL_NAME = "gemini-2.5-flash"

genai.configure(api_key=GEMINI_API_KEY)

# ============================================
# PDF PROCESSING
# ============================================
def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file"""
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_file.getvalue()))
        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
    return text

# ============================================
# DDR GENERATION WITH GEMINI
# ============================================
def generate_ddr_report(inspection_text, thermal_text):
    """
    Send both reports to Gemini and generate structured DDR
    """
    
    prompt = f"""
You are a professional building diagnostics engineer. Create a Detailed Diagnostic Report (DDR) 
by combining the inspection report and thermal imaging report below.

**CRITICAL RULES (MUST FOLLOW):**
1. NEVER invent facts. If information is missing → write "Not Available"
2. If you find conflicting information → explicitly state the conflict
3. Use SIMPLE, client-friendly language. NO technical jargon
4. Combine thermal findings with inspection observations logically
5. Remove duplicate observations
6. Follow the EXACT output structure shown below

**INPUT DOCUMENTS:**

--- INSPECTION REPORT ---
{inspection_text}
--- END INSPECTION REPORT ---

--- THERMAL REPORT ---
{thermal_text}
--- END THERMAL REPORT ---

**OUTPUT STRUCTURE (use these exact headings):**

# DETAILED DIAGNOSTIC REPORT (DDR)
Generated: {datetime.now().strftime('%Y-%m-%d')}

## 1. Property Issue Summary
[Write 3-5 sentences summarizing ALL identified issues from BOTH reports]

## 2. Area-wise Observations
[List each area/room separately]
- **Area Name**: 
  - Observations from inspection:
  - Thermal findings:
  - Combined assessment:

## 3. Probable Root Cause
[For each major issue, state the most likely cause based on evidence]

## 4. Severity Assessment (with reasoning)
[List each issue with severity: HIGH / MEDIUM / LOW and brief reasoning]

## 5. Recommended Actions
[Specific, actionable steps for each issue]

## 6. Additional Notes
[Any other relevant observations or context]

## 7. Missing or Unclear Information
[Explicitly list what is missing, unclear, or conflicting]
- Missing information: [list or "Not Available"]
- Conflicting information: [list or "Not Available"]
- Unclear details: [list or "Not Available"]

Generate the complete report now.
"""
    
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating report: {str(e)}"

# ============================================
# STREAMLIT UI
# ============================================
def main():
    # Header
    st.title("🏠 Detailed Diagnostic Report (DDR) Generator")
    st.markdown("""
    Upload your **Inspection Report** and **Thermal Report** PDFs to generate a 
    professional, client-ready DDR report using **Gemini 2.5 Flash**.
    """)
    
    # Sidebar
    with st.sidebar:
        st.header("📋 Assignment Requirements")
        st.markdown("""
        **Output Structure:**
        1. Property Issue Summary
        2. Area-wise Observations
        3. Probable Root Cause
        4. Severity Assessment
        5. Recommended Actions
        6. Additional Notes
        7. Missing/Unclear Information
        
        **Rules:**
        - No invented facts
        - Note conflicts
        - "Not Available" for missing data
        - Client-friendly language
        - No technical jargon
        """)
        
        st.divider()
        st.markdown("**Built for:** Applied AI Builder Assignment")
        st.markdown(f"**Model:** {MODEL_NAME}")
    
    # Main content - File upload
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📄 Inspection Report")
        inspection_file = st.file_uploader(
            "Upload inspection report (PDF)",
            type=['pdf'],
            key="inspection"
        )
        if inspection_file:
            st.success(f"✅ Loaded: {inspection_file.name}")
    
    with col2:
        st.subheader("🌡️ Thermal Report")
        thermal_file = st.file_uploader(
            "Upload thermal report (PDF)",
            type=['pdf'],
            key="thermal"
        )
        if thermal_file:
            st.success(f"✅ Loaded: {thermal_file.name}")
    
    # Generate button
    if inspection_file and thermal_file:
        if st.button("🚀 Generate DDR Report", type="primary", use_container_width=True):
            
            # Progress tracking
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Step 1: Extract text
            status_text.text("📖 Extracting text from PDFs...")
            progress_bar.progress(20)
            
            inspection_text = extract_text_from_pdf(inspection_file)
            thermal_text = extract_text_from_pdf(thermal_file)
            
            if not inspection_text.strip() or not thermal_text.strip():
                st.error("❌ Could not extract text from PDFs. Ensure they are not scanned images.")
                return
            
            # Step 2: Generate report
            status_text.text("🤖 Gemini 2.5 Flash is analyzing reports and generating DDR...")
            progress_bar.progress(50)
            
            with st.spinner("This takes 20-30 seconds..."):
                report = generate_ddr_report(inspection_text, thermal_text)
            
            progress_bar.progress(90)
            
            # Step 3: Display report
            status_text.text("📋 Formatting report...")
            
            # Store in session state
            st.session_state['report'] = report
            st.session_state['report_generated'] = True
            
            progress_bar.progress(100)
            status_text.text("✅ DDR Report generated successfully!")
            time.sleep(1)
            status_text.empty()
            progress_bar.empty()
    
    # Display report if generated
    if 'report_generated' in st.session_state and st.session_state['report_generated']:
        st.divider()
        st.header("📑 Generated DDR Report")
        
        # Download button
        st.download_button(
            label="📥 Download DDR Report (TXT)",
            data=st.session_state['report'],
            file_name=f"DDR_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True
        )
        
        # Display report in expander
        with st.expander("📄 View Full Report", expanded=True):
            st.markdown(st.session_state['report'])
        
        # Validation check
        st.divider()
        st.subheader("🔍 Assignment Compliance Check")
        
        # Check for "Not Available"
        if "Not Available" in st.session_state['report']:
            st.success("✅ 'Not Available' used for missing information")
        else:
            st.warning("⚠️ No 'Not Available' statements found - verify missing data is flagged")
        
        # Check sections
        required_sections = [
            "1. Property Issue Summary",
            "2. Area-wise Observations",
            "3. Probable Root Cause",
            "4. Severity Assessment",
            "5. Recommended Actions",
            "6. Additional Notes",
            "7. Missing or Unclear Information"
        ]
        
        for section in required_sections:
            if section in st.session_state['report']:
                st.success(f"✅ {section}")
            else:
                st.error(f"❌ Missing: {section}")
    
    # Instructions for first-time users
    else:
        st.info("👆 Please upload both PDF reports to generate the DDR report.")
        
        with st.expander("📌 Sample format expectations"):
            st.markdown("""
            **Inspection Report should contain:**
            - Site observations
            - Issue descriptions
            - Area/location references
            
            **Thermal Report should contain:**
            - Temperature readings
            - Thermal anomalies
            - IR image interpretations
            
            Your solution should work on **any** similar reports, not just specific files.
            """)

if __name__ == "__main__":
    main()