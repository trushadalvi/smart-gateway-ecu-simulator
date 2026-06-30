import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StatusFooterComponent } from './status-footer.component';

describe('StatusFooterComponent', () => {
  let component: StatusFooterComponent;
  let fixture: ComponentFixture<StatusFooterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [StatusFooterComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StatusFooterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
