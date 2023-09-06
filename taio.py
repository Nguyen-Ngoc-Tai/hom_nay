package bai1;
import java.util.Scanner;
import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;

public class baith3 {
	
	public static void main(String[] args) {
		String HovaTen = null,NgaySinh,GioiTinh,NgayBatDauDiLam,NgayNghiHuu;
		Scanner sc = new Scanner(System.in);
		//khai bao dinh nghia mot dinh dang ngay thang
		DateTimeFormatter df = DateTimeFormatter.ofPattern("dd/MM/yyyy");
		System.out.println("Nhap vao ho va ten : " + HovaTen);
		HovaTen = sc.nextLine();
		System.out.println("Nhap ngay sinh (dd/MM/yyyy):");
		NgaySinh = sc.nextLine();
		System.out.println("Nhap gioi tinh(Nam/Nu):");
		GioiTinh = sc.nextLine();
		System.out.println("Ngay bat dau di lam:");
		NgayBatDauDiLam = sc.nextLine();
		LocalDate ns = LocalDate.parse(NgaySinh,df);
		LocalDate now = LocalDate.now();
		LocalDate ndl = LocalDate.parse(NgayBatDauDiLam,df);
		LocalDate no = LocalDate.now();
	
		// tinh tuoi chinh xac theo ngay 
		Period diff = Period.between(ns, now);
		System.out.println("Ho va ten  : " + HovaTen);
		System.out.println("Tuoi chinh xac : "+ diff.getYears()+ "tuoi" + diff.getMonths() + "thang" + diff.getDays() + "ngay");
		System.out.println("Thoi gian di lam la : " + diff.getYears()+ "nam" + diff.getMonths() + "thang" + diff.getDays() + "ngay");
		//tinh ngay nghi huu

	}
}