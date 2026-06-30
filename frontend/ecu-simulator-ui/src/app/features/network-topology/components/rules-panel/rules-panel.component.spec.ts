import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RulesPanelComponent } from './rules-panel.component';

describe('RulesPanelComponent', () => {
  let component: RulesPanelComponent;
  let fixture: ComponentFixture<RulesPanelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RulesPanelComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RulesPanelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
