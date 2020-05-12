import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { PageNedirPage } from './page-nedir.page';

describe('PageNedirPage', () => {
  let component: PageNedirPage;
  let fixture: ComponentFixture<PageNedirPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PageNedirPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(PageNedirPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
