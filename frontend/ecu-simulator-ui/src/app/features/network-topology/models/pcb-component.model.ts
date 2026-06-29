export type ComponentStatus =
  | 'healthy'
  | 'warning'
  | 'fault';

export type ComponentType =
  | 'power'
  | 'mcu'
  | 'memory'
  | 'can-controller'
  | 'transceiver'
  | 'connector';

export interface PcbComponent {
  id: string;

  name: string;

  type: ComponentType;

  x: number;
  y: number;

  status: ComponentStatus;

  description?: string;
}