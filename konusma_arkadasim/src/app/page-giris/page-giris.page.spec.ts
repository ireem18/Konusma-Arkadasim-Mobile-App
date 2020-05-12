import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { PageGirisPage } from './page-giris.page';

describe('PageGirisPage', () => {
  let component: PageGirisPage;
  let fixture: ComponentFixture<PageGirisPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PageGirisPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(PageGirisPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
