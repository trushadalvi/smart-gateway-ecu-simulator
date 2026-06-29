# SMART GATEWAY ECU SIMULATOR - FRONTEND ARCHITECTURE

## 1. PROJECT OVERVIEW

This is a professional automotive ECU simulator dashboard designed to demonstrate:
- Real-time vehicle state management
- Gateway ECU decision logic and rule evaluation
- CAN bus message traffic monitoring
- Vehicle network topology visualization
- Rule engine configuration

**Target:** Portfolio-worthy, professional engineering dashboard similar to Vector CANoe, ETAS INCA

---

## 2. TECHNOLOGY STACK

- **Framework:** Angular 19+ (Standalone Components)
- **Styling:** SCSS with CSS custom properties (variables)
- **State Management:** RxJS Signals (Angular 19+)
- **API Communication:** HttpClient + WebSocket (ready from backend)
- **Visualization:** Canvas/SVG for network topology
- **UI Components:** Custom-built (no heavy UI libraries for control)

---

## 3. FOLDER STRUCTURE

```
frontend/ecu-simulator-ui/src/app/
├── layouts/
│   ├── main-layout/                 # Main dashboard layout with navigation
│   └── main-layout.component.ts
│
├── pages/
│   ├── dashboard/
│   │   └── dashboard.component.ts   # PAGE 1: Vehicle Control Dashboard
│   ├── can-monitor/
│   │   └── can-monitor.component.ts # PAGE 2: Live CAN Monitor
│   ├── network-topology/
│   │   └── network-topology.component.ts # PAGE 3: Vehicle Network Diagram
│   ├── rules-editor/
│   │   └── rules-editor.component.ts    # PAGE 4: Gateway Rules Editor
│   └── analytics/
│       └── analytics.component.ts       # PAGE 5: CAN Traffic Analytics
│
├── components/
│   ├── ecu-card/                    # Reusable ECU control card
│   │   ├── ecu-card.component.ts
│   │   └── ecu-card.component.scss
│   ├── system-status-card/          # System status summary
│   │   ├── system-status-card.component.ts
│   │   └── system-status-card.component.scss
│   ├── can-table/                   # Reusable CAN message table
│   │   ├── can-table.component.ts
│   │   └── can-table.component.scss
│   ├── network-diagram/             # ECU network visualization
│   │   ├── network-diagram.component.ts
│   │   └── network-diagram.component.scss
│   ├── rule-card/                   # Individual rule display/editor
│   │   ├── rule-card.component.ts
│   │   └── rule-card.component.scss
│   └── speed-slider/                # Speed control component
│       ├── speed-slider.component.ts
│       └── speed-slider.component.scss
│
├── services/
│   ├── vehicle-api.service.ts       # HTTP API calls (extend existing)
│   ├── websocket.service.ts         # WebSocket management
│   ├── vehicle-state.service.ts     # State management with Signals
│   └── rule-engine.service.ts       # Rule engine logic handling
│
├── models/
│   ├── vehicle.model.ts             # VehicleState interface
│   ├── can-message.model.ts         # CANMessage interface
│   └── rule.model.ts                # Rule interface
│
├── utils/
│   ├── status-colors.ts             # Color mapping utility
│   └── ecu-definitions.ts           # ECU configuration data
│
├── app.component.ts                 # Root component
├── app.routes.ts                    # Routing configuration (update)
├── app.config.ts                    # App configuration
└── styles.scss                      # Global styles (update with theme)
```

---

## 4. DATA MODELS

### VehicleState
```typescript
interface VehicleState {
  door_state: 'OPEN' | 'CLOSED';
  brake_state: 'PRESSED' | 'RELEASED';
  engine_state: 'RUNNING' | 'STOPPED';
  headlamp_state: 'ON' | 'OFF';
  speed: number;
  battery_state: 'HEALTHY' | 'FAULT';
  telematics_state: 'ACTIVE' | 'INACTIVE';
  speed_ecu_active: boolean;
  system_ready: boolean;
}
```

### CANMessage
```typescript
interface CANMessage {
  timestamp: string;
  can_id: string;
  source: string;
  data: string;
}
```

### GatewayRule
```typescript
interface GatewayRule {
  id: string;
  name: string;
  description: string;
  condition: string;
  action: string;
  enabled: boolean;
}
```

---

## 5. SERVICE LAYER

### VehicleApiService (Extend)
- `closeDoor()` / `openDoor()`
- `pressBrake()` / `releaseBrake()`
- `batteryHealthy()` / `batteryFault()`
- `setSpeed(value: number)`
- `getVehicleStatus()`
- `getCANMessages()`

### WebSocketService (New)
- Establish WebSocket connection to `ws://localhost:8000/ws`
- Emit live CAN messages via Observable
- Handle reconnection logic
- Clean up on component destroy

### VehicleStateService (New)
- Maintain vehicle state using Angular Signals
- Subscribe to API for initial state
- Subscribe to WebSocket for real-time updates
- Expose state as readonly signals for components

### RuleEngineService (New)
- Fetch rules from backend (if endpoint created)
- Local rule evaluation display
- Rule enable/disable logic
- Trigger actions based on rules

---

## 6. ROUTING STRUCTURE

```
/dashboard          → Vehicle Control Dashboard (PAGE 1)
/can-monitor       → Live CAN Monitor (PAGE 2)
/network-topology  → Vehicle Network Diagram (PAGE 3)
/rules-editor      → Gateway Rules Editor (PAGE 4)
/analytics         → CAN Traffic Analytics (PAGE 5)
```

---

## 7. DESIGN SYSTEM

### Color Palette (Dark Automotive Theme)
```scss
// Backgrounds
--bg-primary: #0f1419;      // Main background
--bg-secondary: #1a1f26;    // Card backgrounds
--bg-tertiary: #232936;     // Input backgrounds

// Text
--text-primary: #e8eef5;    // Main text
--text-secondary: #a8aeb8;  // Secondary text
--text-tertiary: #6f7782;   // Tertiary text

// Status Colors
--status-green: #4ade80;    // Healthy/Running
--status-red: #f87171;      // Fault/Stopped
--status-blue: #3b82f6;     // Active
--status-yellow: #facc15;   // Warning

// Accents
--accent-primary: #3b82f6;  // Primary action
--accent-secondary: #8b5cf6; // Secondary action
--border-color: #2d3748;    // Borders

// Glassmorphism
--glass-bg: rgba(26, 31, 38, 0.5);
--glass-border: rgba(139, 92, 246, 0.1);
```

### Typography
```scss
// Headings
--font-h1: 28px, 700, 1.2
--font-h2: 22px, 600, 1.3
--font-h3: 18px, 600, 1.4

// Body
--font-body: 14px, 400, 1.5
--font-label: 12px, 500, 1.4
--font-mono: 12px, 400, 1.5 (monospace for CAN IDs)
```

### Component Styles
- **Cards:** Glassmorphic with backdrop blur, rounded corners, subtle borders
- **Buttons:** Modern gradients, hover effects, disabled states
- **Inputs:** Transparent background with colored borders on focus
- **Tables:** Striped rows, hover effects, monospace for technical data
- **Animations:** Smooth transitions, CAN message pulse effects

---

## 8. KEY FEATURES BY PAGE

### PAGE 1: Vehicle Control Dashboard
- **ECU Control Cards:** Door, Brake, Battery, Speed ECU
- **System Status Card:** Engine, System Ready, Gateway Active, CAN Traffic Count
- **Real-time Updates:** Reflect all state changes immediately
- **Responsive Grid:** 2-3 columns on desktop, 1 column on mobile

### PAGE 2: Live CAN Monitor
- **Professional Table:** Timestamp, CAN ID, Source ECU, Message Data
- **WebSocket Streaming:** Auto-scroll to newest messages
- **Filtering:** Filter by source ECU
- **Export:** Copy message history to clipboard
- **Message Count:** Live count indicator

### PAGE 3: Vehicle Network Topology
- **ECU Layout:** Hexagonal/grid arrangement showing all ECUs
- **Gateway Central:** Gateway ECU as centerpiece
- **CAN Lines:** Visual connections between ECUs
- **Message Animation:** Animated lines on CAN traffic
- **Legend:** Color-coded ECU types

### PAGE 4: Gateway Rules Editor
- **Rule Display:** Show all 5 current rules with conditions and actions
- **Rule Cards:** Enable/disable toggle, edit buttons
- **Visual Condition Building:** IF-THEN structure clearly visible
- **Add Rule UI:** Interface to create custom rules (placeholder)

### PAGE 5: CAN Traffic Analytics
- **Message Count Chart:** Total messages over time
- **ECU Activity Chart:** Messages by source ECU
- **Traffic Timeline:** Message frequency histogram
- **Statistics Panel:** Total messages, active ECUs, average frequency

---

## 9. STATE MANAGEMENT WITH SIGNALS

```typescript
// VehicleStateService
readonly vehicleState = signal<VehicleState>(initialState);
readonly canMessages = signal<CANMessage[]>([]);
readonly isConnected = signal<boolean>(false);

// Auto-update from API and WebSocket
constructor(api: VehicleApiService, ws: WebSocketService) {
  api.getVehicleStatus().subscribe(state => {
    this.vehicleState.set(state);
  });
  
  ws.messages$.subscribe(msg => {
    this.canMessages.update(msgs => [msg, ...msgs].slice(0, 500));
  });
}
```

---

## 10. IMPLEMENTATION PHASES

### Phase 1: Setup & Foundation
- Create folder structure
- Set up data models and services
- Implement main layout and routing
- Configure global styles and theme

### Phase 2: Core Dashboard (PAGE 1)
- Build ECU cards component
- Build system status card
- Integrate API calls
- Add real-time state updates

### Phase 3: CAN Monitoring (PAGE 2)
- Build CAN table component
- Integrate WebSocket service
- Add message streaming
- Add filtering and sorting

### Phase 4: Network Topology (PAGE 3)
- Canvas/SVG ECU visualization
- CAN line rendering
- Message animation logic
- Responsive scaling

### Phase 5: Rules Editor (PAGE 4)
- Rule display cards
- Enable/disable logic
- Rule editing interface (basic)

### Phase 6: Analytics (PAGE 5)
- Chart integration
- Real-time data aggregation
- Traffic timeline visualization

### Phase 7: Polish & Optimization
- Responsive refinements
- Animation smoothing
- Performance optimization
- Cross-browser testing

---

## 11. RESPONSIVE DESIGN BREAKPOINTS

```scss
// Mobile First
--mobile: 320px
--tablet: 768px
--desktop: 1024px
--wide: 1440px

// Layout adjustments
// Mobile: 1 column, full-width cards
// Tablet: 2 columns, optimized spacing
// Desktop: 3-4 columns, full UI
// Wide: 4+ columns with sidebars
```

---

## 12. LEARNING OBJECTIVES

During implementation, you'll learn:
1. **Angular 19 Signals API** for reactive state management
2. **WebSocket integration** for real-time data
3. **Canvas/SVG rendering** for network visualization
4. **SCSS architecture** with variables and modular styling
5. **Responsive design** principles
6. **Component composition** and reusability
7. **RxJS Observables** for async operations
8. **Professional UI/UX design** patterns

---

## 13. NEXT STEPS

1. **Approve this architecture**
2. **Phase 1 Implementation:** Folder structure, services, models, styles
3. **Phase 2 Implementation:** Vehicle control dashboard (PAGE 1)
4. Continue with remaining phases based on priorities

---
