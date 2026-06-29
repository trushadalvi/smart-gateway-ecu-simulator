import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

import { PcbBoardComponent } from '../../components/pcb-board/pcb-board.component';

@Component({
  selector: 'app-network-topology',
  standalone: true,
  imports: [
    CommonModule,
    PcbBoardComponent
  ],
  templateUrl: './network-topology.component.html',
  styleUrl: './network-topology.component.scss'
})
export class NetworkTopologyComponent {

}