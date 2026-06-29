# Vehicle Control Dashboard - Test Verification Guide

## ✅ Server Status

**Dev Server:** Running on `http://localhost:4200`
**Angular Build:** Successful (0 errors)
**Backend:** Should be running on `http://localhost:8000`
**WebSocket:** `ws://localhost:8000/ws`

---

## 🧪 Test Cases

### Test 1: Dashboard Page Loads
**Steps:**
1. Open browser and navigate to `http://localhost:4200`
2. Verify you see "Vehicle Control Dashboard" header
3. Check sidebar displays all 5 pages
4. Verify dark theme loads correctly

**Expected Results:**
- ✅ Dashboard page loads without errors
- ✅ Dark theme with blue accents visible
- ✅ Responsive layout looks good on your screen
- ✅ WebSocket connection status badge shows connection state

---

### Test 2: System Status Card
**Steps:**
1. Observe the "System Status" card at top of dashboard
2. Check values for:
   - Engine (should show STOPPED initially)
   - System Ready (should show NOT READY)
   - Gateway (should show ACTIVE if backend running)
   - CAN Traffic (should show count - initially 0)

**Expected Results:**
- ✅ All status indicators visible with correct colors
- ✅ Status dots pulse/animate
- ✅ CAN traffic count displays as large number
- ✅ Card has glassmorphic appearance with gradient

---

### Test 3: Door ECU Control
**Steps:**
1. Find the "Door ECU" card (first in grid)
2. Current status should show "CLOSED"
3. Click **OPEN** button
4. Observe status change to "OPEN"
5. Click **CLOSE** button
6. Observe status change back to "CLOSED"

**Expected Results:**
- ✅ Status updates immediately on button click
- ✅ Buttons are responsive with hover effects
- ✅ Loading spinner appears briefly during API call
- ✅ Status color remains consistent (green for CLOSED, yellow for OPEN)

---

### Test 4: Brake ECU Control
**Steps:**
1. Find the "Brake ECU" card (second in grid)
2. Current status should show "RELEASED"
3. Click **PRESS** button
4. Observe status change to "PRESSED"
5. Click **RELEASE** button
6. Observe status change back to "RELEASED"

**Expected Results:**
- ✅ Status updates immediately
- ✅ PRESS button shows red/danger styling
- ✅ Button interactions work smoothly
- ✅ CAN traffic count increases with each action

---

### Test 5: Battery ECU Control
**Steps:**
1. Find the "Battery ECU" card (third in grid)
2. Current status should show "HEALTHY"
3. Click **FAULT** button
4. Observe status change to "FAULT"
5. Watch System Status card - "Telematics" should change to INACTIVE
6. Click **HEALTHY** button
7. Observe status change back to "HEALTHY"
8. Telematics should become ACTIVE (if engine is running)

**Expected Results:**
- ✅ Status updates correctly
- ✅ Related system states react (telematics depends on battery)
- ✅ Color coding reflects health status
- ✅ Gateway rules trigger dependent state changes

---

### Test 6: Speed Control (0-200 km/h)
**Steps:**
1. Find the "Speed Control" card (fourth, full-width)
2. Observe circular gauge showing 0 km/h
3. Drag the slider to 50 km/h
4. Observe gauge updates in real-time
5. Try the +/− buttons to adjust by 5 km/h
6. Enter 150 directly in the input field
7. Click Reset to return to 0

**Expected Results:**
- ✅ Gauge updates smoothly with slider
- ✅ Slider track shows color gradient (red→yellow→green)
- ✅ All three input methods work (slider, buttons, text input)
- ✅ Speed ECU status activates at any speed > 0
- ✅ Status updates in info section below

---

### Test 7: Gateway Rule Execution
**Steps:**
1. Set speed to 0, brake RELEASED, door OPEN, battery HEALTHY
2. Close door: Click Door "CLOSE"
3. Press brake: Click Brake "PRESS"
4. Observe system status:
   - Engine should become RUNNING
   - Headlamp should become ON
   - System Ready should still be NOT READY (no speed)
5. Move speed slider to 60 km/h
6. Observe System Ready becomes READY
7. Check additional info section updates

**Expected Results:**
- ✅ Door Closed + Brake Pressed → Engine Starts (Rule 1)
- ✅ Engine Running → Headlamp On (Rule 2)
- ✅ Engine + Battery Healthy → Telematics Active (Rule 3)
- ✅ Speed > 0 → Speed ECU Active (Rule 4)
- ✅ All conditions met → System Ready (Rule 5)

---

### Test 8: CAN Message Count
**Steps:**
1. Note the CAN Traffic count in System Status card
2. Perform 5 actions (clicks, slider moves)
3. Watch CAN Traffic count increase
4. Navigate to Analytics page
5. Verify ECU Activity stats show which ECUs sent messages

**Expected Results:**
- ✅ CAN Traffic count increases with each action
- ✅ Messages are flowing through the backend
- ✅ WebSocket is streaming messages in real-time
- ✅ Analytics page shows which ECUs are active

---

### Test 9: WebSocket Connection
**Steps:**
1. Look at connection badge in top-right
2. Badge should show "🟢 Connected" in green
3. (Optional) Stop backend temporarily
4. Observe badge changes to "🔴 Offline" in red
5. Restart backend
6. Observe reconnection (may take 3 seconds)

**Expected Results:**
- ✅ Connection status displays correctly
- ✅ Badge shows live connection state
- ✅ Auto-reconnect works if connection drops
- ✅ No errors in browser console

---

### Test 10: Navigation & Responsiveness
**Steps:**
1. Click each page in sidebar:
   - Dashboard ✅
   - CAN Monitor ✅ (placeholder)
   - Network Topology ✅ (placeholder)
   - Rules Editor ✅ (functional)
   - Analytics ✅ (partial)
2. Verify each page loads correctly
3. On mobile/tablet, open hamburger menu
4. Verify responsive layout works

**Expected Results:**
- ✅ All pages load without errors
- ✅ Navigation highlights active page
- ✅ Sidebar overlay appears on mobile
- ✅ Content adapts to screen size
- ✅ No console errors

---

## 📊 Browser Console Checks

While testing, open Developer Tools (F12) and check **Console** for:

**You should see:**
- ✅ "WebSocket connected" message
- ✅ API calls returning 200 status
- ✅ No red error messages

**You should NOT see:**
- ❌ CORS errors
- ❌ "WebSocket connection failed" 
- ❌ Uncaught exceptions
- ❌ 404/500 errors

---

## 🎨 Visual Verification

Check these styling elements:

1. **Colors:**
   - ✅ Dark background (#0f1419)
   - ✅ Blue accents (#3b82f6)
   - ✅ Green for healthy (#4ade80)
   - ✅ Red for faults (#f87171)

2. **Effects:**
   - ✅ Pulsing status dots
   - ✅ Hover effects on cards
   - ✅ Smooth transitions on button clicks
   - ✅ Glassmorphic card appearance

3. **Typography:**
   - ✅ Clear hierarchical text sizes
   - ✅ Readable in dark theme
   - ✅ Proper spacing and alignment

4. **Layout:**
   - ✅ Responsive grid (3 cols desktop, 1 mobile)
   - ✅ Cards properly spaced
   - ✅ No text overflow
   - ✅ Icons display correctly

---

## ✅ Sign-Off Checklist

- [ ] Dashboard loads successfully
- [ ] All ECU cards functional
- [ ] Speed slider works smoothly
- [ ] Gateway rules execute in correct order
- [ ] CAN message count increases
- [ ] WebSocket connected badge shows correct status
- [ ] Navigation works to all pages
- [ ] Responsive design works on your screen
- [ ] No console errors
- [ ] Dark theme displays correctly

---

## 📝 Notes for Next Phases

Once dashboard is verified working:

**Phase 3 (CAN Monitor):**
- Will display all CAN messages in professional table
- Real-time updates from WebSocket
- Filtering and sorting capabilities

**Phase 4 (Network Topology):**
- SVG visualization of ECU network
- Animated message flow between components
- Interactive connection highlighting

**Phase 5 (Analytics):**
- Real charts showing traffic patterns
- ECU activity breakdown
- Message frequency analysis

---
