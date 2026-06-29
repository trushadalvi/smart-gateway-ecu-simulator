import { PcbComponent } from '../models/pcb-component.model';

export const BOARD_LAYOUT: PcbComponent[] = [
  {
    id: 'power',
    name: 'TPS54360',
    type: 'power',
    x: 100,
    y: 80,
    status: 'healthy'
  },
  
  {
  id: 'vin',
  name: '12V IN',
  type: 'connector',
  x: 40,
  y: 180,
  status: 'healthy'
},

  {
    id: 'rh850',
    name: 'RH850/F1L',
    type: 'mcu',
    x: 500,
    y: 180,
    status: 'healthy'
  },

  {
    id: 'crystal',
    name: '20 MHz Crystal',
    type: 'memory',
    x: 500,
    y: 100,
    status: 'healthy'
  },

  {
    id: 'eeprom',
    name: 'EEPROM',
    type: 'memory',
    x: 650,
    y: 180,
    status: 'healthy'
  },

  {
    id: 'mcp1',
    name: 'MCP2515 #1',
    type: 'can-controller',
    x: 150,
    y: 350,
    status: 'healthy'
  },

  {
    id: 'mcp2',
    name: 'MCP2515 #2',
    type: 'can-controller',
    x: 300,
    y: 350,
    status: 'healthy'
  },

  {
    id: 'mcp3',
    name: 'MCP2515 #3',
    type: 'can-controller',
    x: 450,
    y: 350,
    status: 'healthy'
  },

  {
    id: 'mcp4',
    name: 'MCP2515 #4',
    type: 'can-controller',
    x: 600,
    y: 350,
    status: 'healthy'
  },

  {
    id: 'mcp5',
    name: 'MCP2515 #5',
    type: 'can-controller',
    x: 750,
    y: 350,
    status: 'healthy'
  },

  {
    id: 'mcp6',
    name: 'MCP2515 #6',
    type: 'can-controller',
    x: 900,
    y: 350,
    status: 'healthy'
  },

  {
    id: 'tja1',
    name: 'TJA1051 #1',
    type: 'transceiver',
    x: 150,
    y: 500,
    status: 'healthy'
  },

  {
    id: 'tja2',
    name: 'TJA1051 #2',
    type: 'transceiver',
    x: 300,
    y: 500,
    status: 'healthy'
  },

  {
    id: 'tja3',
    name: 'TJA1051 #3',
    type: 'transceiver',
    x: 450,
    y: 500,
    status: 'healthy'
  },

  {
    id: 'tja4',
    name: 'TJA1051 #4',
    type: 'transceiver',
    x: 600,
    y: 500,
    status: 'healthy'
  },

  {
    id: 'tja5',
    name: 'TJA1051 #5',
    type: 'transceiver',
    x: 750,
    y: 500,
    status: 'healthy'
  },

  {
    id: 'tja6',
    name: 'TJA1051 #6',
    type: 'transceiver',
    x: 900,
    y: 500,
    status: 'healthy'
  },

  {
    id: 'can1',
    name: 'CAN 1',
    type: 'connector',
    x: 150,
    y: 620,
    status: 'healthy'
  },

  {
    id: 'can2',
    name: 'CAN 2',
    type: 'connector',
    x: 300,
    y: 620,
    status: 'healthy'
  },

  {
    id: 'can3',
    name: 'CAN 3',
    type: 'connector',
    x: 450,
    y: 620,
    status: 'healthy'
  },

  {
    id: 'can4',
    name: 'CAN 4',
    type: 'connector',
    x: 600,
    y: 620,
    status: 'healthy'
  },

  {
    id: 'can5',
    name: 'CAN 5',
    type: 'connector',
    x: 750,
    y: 620,
    status: 'healthy'
  },

  {
    id: 'can6',
    name: 'CAN 6',
    type: 'connector',
    x: 900,
    y: 620,
    status: 'healthy'
  }
];
