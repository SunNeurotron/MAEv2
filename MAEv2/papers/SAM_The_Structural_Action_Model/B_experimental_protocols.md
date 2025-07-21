## **Appendix B: Experimental Protocols**

### **B.1 Protocol for Measuring η in Biological Systems**

**Equipment**:
- Multi-electrode array (MEA) system
- Microcalorimeter
- Neuronal culture preparation

**Procedure**:
1. Prepare neuronal culture on MEA
2. Allow 14-21 days for network maturation
3. Begin simultaneous recording:
   - Heat production via microcalorimetry → ⟨E_dissipated⟩
   - Spike activity via MEA → spike rate
4. Calculate information rate:
   - dN_info/dt ≈ spike_rate × log₂(possible_states)
5. Compute efficiency:
   - η = (dN_info/dt·k_B T ln(2))/⟨E_dissipated⟩
6. Repeat under various conditions (stimulation, stress, drugs)

**Expected Results**:
- Healthy culture: η ≈ 0.1-0.3
- Under stimulation: η increases
- Under stress: η decreases
