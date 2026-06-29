import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

import { BOARD_LAYOUT } from '../../data/gateway-board-layout';
import { PcbComponent } from '../../models/pcb-component.model';

@Component({
  selector: 'app-pcb-board',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './pcb-board.component.html',
  styleUrls: ['./pcb-board.component.scss']
})
export class PcbBoardComponent {

  components: PcbComponent[] = BOARD_LAYOUT;

}